import './css/index.css';

if (!localStorage.getItem('firstVisit')) {
  const notice = document.getElementById('global-notice')!;
  notice.style.display = 'block';

  localStorage.setItem('firstVisit', '1');
}
