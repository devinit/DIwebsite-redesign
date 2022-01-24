export interface PivotTableProps {
  data: Record<string, unknown>[];
  filters: Filter[];
  rowLabel: string;
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
