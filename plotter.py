import plotly.graph_objects as go

class Plotter:
    def __init__(self, df):
        self.df = df

    def plot_null_values(self, before_null_info, after_null_info):
        """Plot the number of NULL values before and after imputation using Plotly."""
        # Get the count of NULL values before and after imputation
        before_nulls = before_null_info['Null Count']
        after_nulls = after_null_info['Null Count']

        # Create a plot with bars for missing values before and after imputation
        fig = go.Figure()

        # Add bars for the missing values before imputation
        fig.add_trace(go.Bar(
            x=before_nulls.index,
            y=before_nulls,
            name='Before',
            marker_color='red',
            opacity=0.6
        ))

        # Add bars for the missing values after imputation
        fig.add_trace(go.Bar(
            x=after_nulls.index,
            y=after_nulls,
            name='After',
            marker_color='green',
            opacity=0.6
        ))

        # Customize the layout to display the counts clearly
        fig.update_layout(
            title='Missing Values Before and After Imputation',
            xaxis_title='Columns',
            yaxis_title='Number of Missing Values',
            barmode='group',
            xaxis_tickangle=-45,
            template='plotly_white',
            height=600,
            width=1000
        )

        # Add a note if no missing values are present in the 'after' dataset
        if after_nulls.sum() == 0:
            fig.add_annotation(
                text="No missing values after imputation.",
                xref="paper", yref="paper",
                showarrow=False,
                font=dict(size=14, color="green")
            )

        # Show the plot
        fig.show()
