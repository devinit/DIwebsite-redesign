import * as localForage from 'localforage';

localForage.config({
  driver: localForage.LOCALSTORAGE,
  name: 'dashboard',
  storeName: 'dashboard-store',
});
