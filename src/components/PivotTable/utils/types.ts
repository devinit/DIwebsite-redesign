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
  rowHighlightField?: string;
  rowHighlightCondition?: HighlightCondition;
  rowHighlightValue?: string;
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
}
