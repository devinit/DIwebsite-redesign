import { createElement } from 'react';
import { render } from 'react-dom';
import { Dashboard } from './Dashboard';
import './utils/localforage';

const rootNode = document.getElementById('root');
if (rootNode) {
  render(createElement(Dashboard), rootNode);
}
