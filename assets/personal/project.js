(() => {
  const tablist = document.querySelector('.platform-tabs');
  if (!tablist) return;
  const tabs = [...tablist.querySelectorAll('[role="tab"]')];
  const image = document.getElementById('platform-screenshot');
  const panel = document.getElementById('screenshot-panel');
  const caption = document.getElementById('screenshot-caption');
  const fullImage = document.getElementById('screenshot-full');
  const views = {
    mac: {
      src: '/assets/personal/assistant-explore.webp',
      alt: 'The native Mac People view, showing connections between fictional records',
      caption: 'Native Mac Explore view. Fictional records used for demonstration.',
      width: 880, height: 999
    },
    iphone: {
      src: '/assets/personal/assistant-iphone.webp',
      alt: 'The native iPhone People view, with a search field and a graph of fictional connections',
      caption: 'The same People view on iPhone. Fictional records used for demonstration.',
      width: 650, height: 1409
    }
  };
  function select(tab) {
    const view = views[tab.dataset.platform];
    if (!view) return;
    tabs.forEach(item => {
      const active = item === tab;
      item.setAttribute('aria-selected', String(active));
      item.tabIndex = active ? 0 : -1;
    });
    panel.setAttribute('aria-labelledby', tab.id);
    panel.classList.toggle('is-phone', tab.dataset.platform === 'iphone');
    image.src = view.src;
    image.alt = view.alt;
    image.width = view.width;
    image.height = view.height;
    caption.textContent = view.caption;
    fullImage.href = view.src;
  }
  tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => select(tab));
    tab.addEventListener('keydown', event => {
      let next;
      if (event.key === 'ArrowRight') next = (index + 1) % tabs.length;
      else if (event.key === 'ArrowLeft') next = (index + tabs.length - 1) % tabs.length;
      else if (event.key === 'Home') next = 0;
      else if (event.key === 'End') next = tabs.length - 1;
      else return;
      event.preventDefault();
      tabs[next].focus();
      select(tabs[next]);
    });
  });
  tablist.hidden = false;
})();
