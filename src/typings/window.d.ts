export {};

declare global {
  interface Window {
    google_optimize: { get: (id: string) => string };
  }
}
