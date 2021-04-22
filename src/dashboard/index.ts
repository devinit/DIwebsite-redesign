import { createElement } from 'react';
import { render } from 'react-dom';
import { AsyncDashboard } from './AsyncDashboardLoader';
import './utils/localforage';

const rootNode = document.getElementById('root');
if (rootNode) {
  render(createElement(AsyncDashboard), rootNode);
}
