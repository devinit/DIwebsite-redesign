import React, { FunctionComponent } from 'react';
import { Card } from './components/Card';
import { Grid } from './components/Grid';

const Dashboard: FunctionComponent = () => {
  return (
    <Grid>
      <Card></Card>
      <Card></Card>
      <Card></Card>
      <Card></Card>
    </Grid>
  );
};

export { Dashboard };
