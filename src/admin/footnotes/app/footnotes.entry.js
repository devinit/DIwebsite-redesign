import '../js/custom-modal-workflow';
import Footnote from '../js/decorators/Footnote';
import FootnoteSource from '../js/sources/FootnoteSource';

// Register the plugin directly on script execution so the editor loads it when initializing.
window.draftail.registerPlugin(
  {
    type: 'FOOTNOTE',
    source: FootnoteSource,
    decorator: Footnote,
  },
  'entityTypes',
);
