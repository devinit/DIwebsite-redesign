export interface PivotTableProps {
  data: Record<string, unknown>[];
  filters: Filter[];
  rowLabel: string;
  rowLabelHeading: string;
  columnLabel: string;
  cellValue: string;
  showRowTotal?: boolean;
  showColumnTotal?: boolean;
  cellHighlightCondition?: HighlightCondition;
  cellHighlightValue?: string;
  rowHighlights?: RowHighlight[];
  rowHighlightField?: string;
  rowHighlightCondition?: HighlightCondition;
  rowHighlightValue?: string;
  rowHighlightColour?: string;
}

export type HighlightCondition = 'lt' | 'gt' | 'lte' | 'gte' | 'eq';

export interface Filter {
  name: string;
  value?: string;
}

export interface RowHighlight {
  field?: string;
  condition?: HighlightCondition;
  value?: string | number;
  color?: string;
}

export interface HighlightedRow {
  label: string;
  color: string;
}
