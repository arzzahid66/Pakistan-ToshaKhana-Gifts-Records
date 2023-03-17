import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
st.title(" Pakistan ToshaKhana Gifts Records")
st.subheader("From 2002 to 2023")
st.subheader("Visualization by : Abdul_Rehman_Zahid & Abdul_Rehman")
# Small title
st.write("Portfolio A_R_Z : https://arzzahid66.github.io/arcodes/")
st.write("Portfolio A_R : https://abdulrehman1232.github.io/portfolio/")
st.write("Dataset link  :https://www.scribd.com/document/630951780/TK-Record-1-2#")
df = pd.read_csv("Refined_TK_data.csv")
df = df.rename(columns=lambda x: x.replace(' ', '_'))
# Define a custom color palette
# Define the custom color palette
colors = ["#FFC300", "#FF5733", "#C70039", "#900C3F", "#581845"]

# Create the Plotly figure with the custom color palette
fig = px.bar(df, x="Affiliation", y="Assessed_Value", color='Retention_Cost',
             color_discrete_sequence=colors, barmode='group', height=400)

# Update the figure layout with the centered title
fig.update_layout(
    title={
        'text': 'Top 10 Most Valued Gifts Retained by ToshaKhana with Retention Cost',
        'font': {'size': 20},
        'x':0.5, # Center the title horizontally
        'y':0.95, # Adjust the title position vertically
        'xanchor': 'center', # Anchor the title to the center
        'yanchor': 'top' # Anchor the title to the top of the plot
    }
)

# Display the Plotly figure in Streamlit
st.plotly_chart(fig)

# sort the dataframe by 'Assessed_Value' in descending order
sorted_df = df.sort_values(by='Assessed_Value', ascending=False)

# select the top 5 rows using the nlargest() method
top_10_df = sorted_df.nlargest(10, 'Assessed_Value')

# print the 'Detail_of_Gifts' column of the top 5 rows
top_10_gift=top_10_df['Detail_of_Gifts']

top_10_name_of_reci = top_10_df['Name_of_Recipient']

top_10_Assessed = top_10_df['Assessed_Value']

top_10_Retention_Cost = top_10_df['Retention_Cost']

top_10_Remarks = top_10_df['Remarks']
top_10_Affiliation = top_10_df['Affiliation']
top_10_Date = top_10_df['Date']
# create a dataframe from the top 10 rows
top_10_df = sorted_df.nlargest(10, 'Assessed_Value')

# create the bubble chart
fig = px.scatter(top_10_df, x='Assessed_Value', y='Retention_Cost',
                 size='Assessed_Value', color='Affiliation',
                 hover_name='Name_of_Recipient',
                 hover_data={'Detail_of_Gifts': True, 'Remarks': True, 'Date': True},
                 size_max=50)

fig.update_layout(
    title={
        'text': 'Top 10 Most Expensive Gifts Recorded by ToshaKhana and Gift Holders',
        'font': {'size': 20}
    },
    title_x=0.5
)
st.plotly_chart(fig)
# Read in the dataset as a Pandas DataFrame

# Calculate the total number of gifts
total_gifts = df.shape[0]

# Get the number of gifts by affiliation
gifts_by_affiliation = df['Affiliation'].value_counts()

# Get the number of gifts retained and with retention cost by affiliation
gifts_with_retention = df[df['Retention_Cost'] > 0]['Affiliation'].value_counts()
gifts_retained = df[df['Retained'] == 'Yes'][['Affiliation', 'Retention_Cost']].groupby('Affiliation').agg({'Retention_Cost': 'count', 'Affiliation': 'size'})
gifts_retained.columns = ['Gifts Retained without Retention Cost', 'Gifts with Retention Cost']

# Create a bar chart of the number of gifts by affiliation
data = [go.Bar(x=gifts_by_affiliation.index, y=gifts_by_affiliation.values)]

# Customize the layout of the chart
layout = go.Layout(title='Most Number of gifts Received ', xaxis=dict(title='Affiliation'), yaxis=dict(title='Number of Gifts'), 
                   title_x=0.5, title_y=0.9)

# Create a Figure object and plot it with Plotly
fig = go.Figure(data=data, layout=layout)
st.plotly_chart(fig)

# Create a table of the number of gifts retained and with retention cost by affiliation
table_data = [go.Table(header=dict(values=['Affiliation', 'Gifts with Retention Cost', 'Gifts Retained without Retention Cost']),
                       cells=dict(values=[gifts_by_affiliation.index, gifts_with_retention.values, gifts_retained['Gifts Retained without Retention Cost'].values]))]

# Create a layout for the table
table_layout = go.Layout(title='Retention Cost vs. Non-Retention Cost: A Comparison of ToshaKhana Gifts', title_x=0.5, title_y=0.9)

# Create a Figure object for the table and plot it with Plotly
table_fig = go.Figure(data=table_data, layout=table_layout)
st.plotly_chart(table_fig)
# top 5 reci received expensive gift 
# sort the dataframe by 'Assessed_Value' in descending order
sorted_df = df.sort_values(by='Assessed_Value', ascending=False)

# select the top 5 rows using the nlargest() method
top_5_df = sorted_df.nlargest(5, 'Assessed_Value')

# print the 'Detail_of_Gifts' column of the top 5 rows
top_5_gift=top_5_df['Detail_of_Gifts']

top_5_name_of_reci = top_5_df['Name_of_Recipient']

top_5_Assessed = top_5_df['Assessed_Value']

top_5_Retention_Cost = top_5_df['Retention_Cost']

top_5_Remarks = top_5_df['Remarks']
top_5_Affiliation = top_5_df['Affiliation']
top_5_Date = top_5_df['Date']
# Create a new dataframe with top 5 recipients by assessed value
top_5_assessed = df.groupby('Name_of_Recipient')['Assessed_Value'].sum().nlargest(5).reset_index()

# Create a bar graph for top 5 recipients by assessed value
assessed_value_fig = go.Figure(
    data=[go.Bar(x=top_5_assessed['Name_of_Recipient'], y=top_5_assessed['Assessed_Value'])]
)
assessed_value_fig.update_layout(
    title='Top 5 Most Valued Gifts Received by Recipients',
    xaxis_title='Name of Recipient',
    yaxis_title='Assessed Value'
)
st.plotly_chart(assessed_value_fig)

# Create a new dataframe with top 5 recipients by retention cost
top_5_retention = df.groupby('Name_of_Recipient')['Retention_Cost'].sum().nlargest(5).reset_index()

# Create a bar graph for top 5 recipients by retention cost
retention_cost_fig = go.Figure(
    data=[go.Bar(x=top_5_retention['Name_of_Recipient'], y=top_5_retention['Retention_Cost'])]
)
retention_cost_fig.update_layout(
    title='Top 5 Recipients who Paid the Highest Retention Cost for ToshaKhana Gifts',
    xaxis_title='Name of Recipient',
    yaxis_title='Retention Cost'
)
st.plotly_chart(retention_cost_fig)

# Create a new dataframe with top 5 recipients by remarks
top_5_remarks = df.groupby('Name_of_Recipient')['Retained'].count().nlargest(5).reset_index()

# Create a bar graph for top 5 recipients by remarks
remarks_fig = go.Figure(
    data=[go.Bar(x=top_5_remarks['Name_of_Recipient'], y=top_5_remarks['Retained'])]
)
remarks_fig.update_layout(
    title='Top 5 Recipients who Retained the Maximum Number of ToshaKhana Gifts',
    xaxis_title='Name of Recipient',
    yaxis_title='Retained'
)
st.plotly_chart(remarks_fig)

fig = px.bar(top_5_df, x='Detail_of_Gifts', y='Assessed_Value',
             hover_data=['Name_of_Recipient'],
             labels={'Detail_of_Gifts': 'Gift', 'Assessed_Value': 'Assessed Value'})
fig.update_layout(title='Top 5 Most Expensive Gifts & Name of Recipient')
st.plotly_chart(fig)





