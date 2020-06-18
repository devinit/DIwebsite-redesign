import 'plotly.js';

declare module "plotly.js" {
    /**
     *  registers individual modules for custom import
     */
    export const register: (modules: any[]) => void;
}
