export const getQuarterYear = (dateString: string): [number, number] => {
  try {
    const date = new Date(dateString);
    const quarter = Math.floor((date.getMonth() + 3) / 3);

    return [quarter, date.getFullYear()];
  } catch (error) {
    return [0, 0];
  }
};

export const colours = ['#6c120a', '#a21e25', '#cd2b2a', '#dc372d', '#ec6250', '#f6b0a0', '#fbd7cb', '#fce3dc'];
