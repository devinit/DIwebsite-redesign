import { makeObservable, observable, action, computed, autorun } from 'mobx';

class State {
  id = Math.random();
  state = {};

  constructor() {
    makeObservable(this, {
      state: observable,
      setState: action,
      getState: computed,
    });
    this.state = {};
  }

  setState(state, merge = true) {
    this.state = merge ? { ...this.state, ...state } : state;
  }

  get getState() {
    console.log(this.state);

    return this.state;
  }
}

const state = new State();
(window as any).DIState = state;

autorun(() => {
  console.log('State: ', state.getState);
});
