import '../js/custom-modal-workflow';
import Footnote from '../js/decorators/Footnote';
import FootnoteSource from '../js/sources/FootnoteSource';

const draftail = window.draftail;

// Plugins for the built-in entities.
const plugins = [
  {
    type: 'FOOTNOTE',
    source: FootnoteSource,
    decorator: Footnote,
  },
];

plugins.forEach(draftail.registerPlugin);
