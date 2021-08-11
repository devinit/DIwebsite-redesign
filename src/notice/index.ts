const getCookie = (key: string) => {
  const keyValue = document.cookie.match(`(^|;) ?${key}=([^;]*)(;|$)`);

  return keyValue ? keyValue[2] : null;
};

const handleNotices = () => {
  const notices = document.querySelectorAll<HTMLDivElement>('[data-notice]');
  Array.prototype.forEach.call(notices, (notice: HTMLDivElement) => {
    const cookieName = notice.getAttribute('id');
    if (cookieName && getCookie(cookieName) === 'dismissed') {
      notice.remove();
    } else {
      notice.classList.remove('display-none');
    }
  });
};

handleNotices();
