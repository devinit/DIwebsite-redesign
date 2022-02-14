import { makeObservable, observable, action, computed, autorun, IReactionDisposer } from 'mobx';

class State {
  id = Math.random();
  state = {};
  listeners: Array<IReactionDisposer | null> = [];

  constructor() {
    makeObservable(this, {
      state: observable,
      setState: action,
      getState: computed,
    });
  }

  setState(state: Record<string, unknown>, merge = true) {
    this.state = merge ? { ...this.state, ...state } : state;
  }

  get getState() {
    return this.state;
  }

  addListener(callback: () => void) {
    this.listeners = this.listeners.concat(autorun(callback));

    return this.listeners.length - 1; // returns index of the added listener - shall be used to remove
  }

  removeListener(index: number) {
    if (index < this.listeners.length && this.listeners[index]) {
      (this.listeners[index] as IReactionDisposer)();
      this.listeners[index] = null;
    }
  }

  resetListeners() {
    this.listeners = [];
  }
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
(window as any).DIState = new State();
