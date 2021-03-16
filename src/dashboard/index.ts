import { createElement } from 'react';
import { render } from 'react-dom';
import { Dashboard } from './Dashboard';

const rootNode = document.getElementById('root');
if (rootNode) {
  render(createElement(Dashboard), rootNode);
}
