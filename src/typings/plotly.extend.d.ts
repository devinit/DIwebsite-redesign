import 'plotly.js';

declare module 'plotly.js' {
  /**
   *  registers individual modules for custom import
   */
  export const register: (modules: any[]) => void; // eslint-disable-line @typescript-eslint/no-explicit-any

  export interface PlotData {
    meta: any; // eslint-disable-line @typescript-eslint/no-explicit-any
  }
}
