// ===== FILE SYSTEM =====
class Node {
    constructor(name, isDir) {
        this.name = name;
        this.isDir = isDir;
        this.content = "";
        this.parent = null;
        this.children = [];
    }
}

let root = new Node("", true);
let currentDir = root;

function addChild(parent, child) {
    child.parent = parent;
    parent.children.push(child);
}

function findChild(dir, name) {
    return dir.children.find(c => c.name === name);
}

// preload
let readme = new Node("readme.txt", false);
readme.content = "Welcome to KalebOS\nType help";
addChild(root, readme);

// ===== TERMINAL =====
const term = document.getElementById("terminal");
const input = document.getElementById("input");

function print(text) {
    term.innerText += text + "\n";
    term.scrollTop = term.scrollHeight;
}

// ===== COMMANDS =====
const commands = {

    help() {
        print(`Commands:
ls cd mkdir touch cat echo pwd
calc encode search clear`);
    },

    ls() {
        print(currentDir.children.map(c => c.name + (c.isDir ? "/" : "")).join("  "));
    },

    cd(args) {
        if (!args) currentDir = root;
        else if (args === "..") currentDir = currentDir.parent || root;
        else {
            let dir = findChild(currentDir, args);
            if (dir && dir.isDir) currentDir = dir;
            else print("No such directory");
        }
    },

    mkdir(args) {
        if (!args) return print("Usage: mkdir <name>");
        if (findChild(currentDir, args)) return print("Exists");
        addChild(currentDir, new Node(args, true));
    },

    touch(args) {
        if (!args) return print("Usage: touch <file>");
        addChild(currentDir, new Node(args, false));
    },

    cat(args) {
        let f = findChild(currentDir, args);
        if (f && !f.isDir) print(f.content);
        else print("No such file");
    },

    echo(args) {
        if (!args.includes(">")) return print(args);
        let [text, file] = args.split(">");
        text = text.trim();
        file = file.trim();

        let f = findChild(currentDir, file);
        if (!f) {
            f = new Node(file, false);
            addChild(currentDir, f);
        }
        f.content = text;
    },

    pwd() {
        let path = "";
        let n = currentDir;
        while (n) {
            path = "/" + n.name + path;
            n = n.parent;
        }
        print(path || "/");
    },

    clear() {
        term.innerText = "";
    },

    search(args) {
        chrome.tabs.create({
            url: "https://www.google.com/search?q=" + encodeURIComponent(args)
        });
    },

    calc() {
        let a = parseFloat(prompt("First number"));
        let b = parseFloat(prompt("Second number"));
        let op = prompt("Operation (+ - * /)");

        let result;
        if (op === "+") result = a + b;
        else if (op === "-") result = a - b;
        else if (op === "*") result = a * b;
        else if (op === "/") result = b === 0 ? "Error" : a / b;

        print("Result: " + result);
    },

    encode() {
        let mode = prompt("1=encode 2=decode");
        let key = parseInt(prompt("key"));
        let text = prompt("text");

        let result = "";
        for (let c of text) {
            if (/[a-z]/i.test(c)) {
                let base = c === c.toUpperCase() ? 65 : 97;
                let shift = mode === "1" ? key : -key;
                result += String.fromCharCode((c.charCodeAt(0) - base + shift + 26) % 26 + base);
            } else result += c;
        }

        print(result);
    }
};

// ===== INPUT =====
input.addEventListener("keydown", function(e) {
    if (e.key === "Enter") {
        let line = input.value;
        print("> " + line);

        let [cmd, ...rest] = line.split(" ");
        let args = rest.join(" ");

        if (commands[cmd]) commands[cmd](args);
        else print("Unknown command");

        input.value = "";
    }
});

// startup
print("Welcome to KalebOS Extension");
print("Type help");