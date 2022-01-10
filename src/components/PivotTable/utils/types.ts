export interface PivotTableProps {
  data: Record<string, unknown>[];
  filters: Filter[];
  rowLabel: string;
  columnLabel: string;
  cellValue: string;
  showRowTotal?: boolean;
  showColumnTotal?: boolean;
}

export interface Filter {
  name: string;
  value?: string;
}