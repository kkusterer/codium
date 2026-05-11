chrome.action.onClicked.addListener(() => {
  chrome.windows.create({
    url: "basic.html",
    type: "popup",
    width: 800,
    height: 600
  });
});