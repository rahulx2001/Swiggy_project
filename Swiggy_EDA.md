Swiggy Restaurant Analysis Notebook



```python
import pandas as pd 
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import squarify
```


```python
df = pd.read_csv("swiggy.csv")
```


```python
df.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Area</th>
      <th>City</th>
      <th>Restaurant</th>
      <th>Price</th>
      <th>Avg ratings</th>
      <th>Total ratings</th>
      <th>Food type</th>
      <th>Address</th>
      <th>Delivery time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>211</td>
      <td>Koramangala</td>
      <td>Bangalore</td>
      <td>Tandoor Hut</td>
      <td>300.0</td>
      <td>4.4</td>
      <td>100</td>
      <td>Biryani,Chinese,North Indian,South Indian</td>
      <td>5Th Block</td>
      <td>59</td>
    </tr>
    <tr>
      <th>1</th>
      <td>221</td>
      <td>Koramangala</td>
      <td>Bangalore</td>
      <td>Tunday Kababi</td>
      <td>300.0</td>
      <td>4.1</td>
      <td>100</td>
      <td>Mughlai,Lucknowi</td>
      <td>5Th Block</td>
      <td>56</td>
    </tr>
    <tr>
      <th>2</th>
      <td>246</td>
      <td>Jogupalya</td>
      <td>Bangalore</td>
      <td>Kim Lee</td>
      <td>650.0</td>
      <td>4.4</td>
      <td>100</td>
      <td>Chinese</td>
      <td>Double Road</td>
      <td>50</td>
    </tr>
    <tr>
      <th>3</th>
      <td>248</td>
      <td>Indiranagar</td>
      <td>Bangalore</td>
      <td>New Punjabi Hotel</td>
      <td>250.0</td>
      <td>3.9</td>
      <td>500</td>
      <td>North Indian,Punjabi,Tandoor,Chinese</td>
      <td>80 Feet Road</td>
      <td>57</td>
    </tr>
    <tr>
      <th>4</th>
      <td>249</td>
      <td>Indiranagar</td>
      <td>Bangalore</td>
      <td>Nh8</td>
      <td>350.0</td>
      <td>4.0</td>
      <td>50</td>
      <td>Rajasthani,Gujarati,North Indian,Snacks,Desser...</td>
      <td>80 Feet Road</td>
      <td>63</td>
    </tr>
    <tr>
      <th>5</th>
      <td>254</td>
      <td>Indiranagar</td>
      <td>Bangalore</td>
      <td>Treat</td>
      <td>800.0</td>
      <td>4.5</td>
      <td>100</td>
      <td>Mughlai,North Indian</td>
      <td>100 Feet Road</td>
      <td>56</td>
    </tr>
    <tr>
      <th>6</th>
      <td>258</td>
      <td>Indiranagar</td>
      <td>Bangalore</td>
      <td>Chinita Real Mexican Food</td>
      <td>1000.0</td>
      <td>4.5</td>
      <td>500</td>
      <td>Mexican,Beverages,Salads</td>
      <td>Double Road</td>
      <td>53</td>
    </tr>
    <tr>
      <th>7</th>
      <td>263</td>
      <td>Koramangala</td>
      <td>Bangalore</td>
      <td>Cupcake Noggins - Cakespastries And Desserts</td>
      <td>150.0</td>
      <td>4.3</td>
      <td>100</td>
      <td>Desserts,British,Bakery,Pizzas,Snacks</td>
      <td>4Th Block</td>
      <td>57</td>
    </tr>
    <tr>
      <th>8</th>
      <td>267</td>
      <td>Domlur</td>
      <td>Bangalore</td>
      <td>Tea Brew</td>
      <td>350.0</td>
      <td>4.1</td>
      <td>100</td>
      <td>American,Italian,Beverages,Continental,Chinese...</td>
      <td>Double Road</td>
      <td>57</td>
    </tr>
    <tr>
      <th>9</th>
      <td>308</td>
      <td>Koramangala</td>
      <td>Bangalore</td>
      <td>Bangaliana</td>
      <td>300.0</td>
      <td>4.0</td>
      <td>500</td>
      <td>Bengali</td>
      <td>7Th Block</td>
      <td>57</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.describe
```




    <bound method NDFrame.describe of           ID                    Area       City                Restaurant  \
    0        211             Koramangala  Bangalore               Tandoor Hut   
    1        221             Koramangala  Bangalore             Tunday Kababi   
    2        246               Jogupalya  Bangalore                   Kim Lee   
    3        248             Indiranagar  Bangalore         New Punjabi Hotel   
    4        249             Indiranagar  Bangalore                       Nh8   
    ...      ...                     ...        ...                       ...   
    8675  464626  Panjarapole Cross Road  Ahmedabad                Malt Pizza   
    8676  465835                  Rohini      Delhi  Jay Mata Ji Home Kitchen   
    8677  465872                  Rohini      Delhi      Chinese Kitchen King   
    8678  465990                  Rohini      Delhi    Shree Ram Paratha Wala   
    8679  466488             Navrangpura  Ahmedabad              Sassy Street   
    
          Price  Avg ratings  Total ratings  \
    0     300.0          4.4            100   
    1     300.0          4.1            100   
    2     650.0          4.4            100   
    3     250.0          3.9            500   
    4     350.0          4.0             50   
    ...     ...          ...            ...   
    8675  500.0          2.9             80   
    8676  200.0          2.9             80   
    8677  150.0          2.9             80   
    8678  150.0          2.9             80   
    8679  250.0          2.9             80   
    
                                                  Food type       Address  \
    0             Biryani,Chinese,North Indian,South Indian     5Th Block   
    1                                      Mughlai,Lucknowi     5Th Block   
    2                                               Chinese   Double Road   
    3                  North Indian,Punjabi,Tandoor,Chinese  80 Feet Road   
    4     Rajasthani,Gujarati,North Indian,Snacks,Desser...  80 Feet Road   
    ...                                                 ...           ...   
    8675                                             Pizzas   Navrangpura   
    8676                                       South Indian        Rohini   
    8677                             Chinese,Snacks,Tandoor        Rohini   
    8678                         North Indian,Indian,Snacks        Rohini   
    8679                               Chaat,Snacks,Chinese   Navrangpura   
    
          Delivery time  
    0                59  
    1                56  
    2                50  
    3                57  
    4                63  
    ...             ...  
    8675             40  
    8676             28  
    8677             58  
    8678             28  
    8679             44  
    
    [8680 rows x 10 columns]>




```python
num_records = len(df)
num_records
```




    8680




```python
df.shape
```




    (8680, 10)




```python
price_range_counts = df['Price'].value_counts()
price_pie =px.pie(price_range_counts, names = price_range_counts.index, values= price_range_counts.values)
price_range_counts.head()

```




    Price
    300.0    1776
    200.0    1774
    250.0     968
    400.0     838
    500.0     605
    Name: count, dtype: int64



Data Analysis

#Correlation between Restaurant Price and Average Rating


```python
# Correlation between restaurant price and average rating
fig = px.scatter(df, x='Price', y='Avg ratings', title='Correlation between Restaurant Price and Average Rating', color_discrete_sequence=['red'])
fig.update_layout(template="plotly_dark")
fig.show()


```
- ![](https://github.com/rahulx2001/Swiggy_project/blob/main/output_10_0.png)


#Most Popular Food Types in Top 10 Cities


```python
# Group by 'City' and 'Food type', then count occurrences
city_food_counts = df.groupby(['City', 'Food type']).size().reset_index(name='Count')

# Find the most popular food type in each city
popular_food_types = city_food_counts.loc[city_food_counts.groupby('City')['Count'].idxmax()]

# Get the top 10 cities with the most popular food types
top_10_cities = popular_food_types.nlargest(10, 'Count')

# Prepare the data for the treemap
labels = top_10_cities['City'] + ' - ' + top_10_cities['Food type']
sizes = top_10_cities['Count']

# Create the treemap
import matplotlib.pyplot as plt
import squarify

plt.figure(figsize=(12, 6))
squarify.plot(sizes=sizes, label=labels, alpha=0.8)

plt.axis('off')
plt.title('Most Popular Food Types in Top 10 Cities')
plt.show()

                                            
```


    
![png](output_12_0.png)
    


Top 10 Cities ordering food from Swiggy 


```python
city_count = df["City"].value_counts()
top_n_cities = city_count.nlargest(10)
vis= px.pie(names=top_n_cities.index, values= top_n_cities.values, title = f'Top 10 Cities Ordering Food from Swiggy',labels={'City': 'City'}, width = 650, height= 650)
fig.update_layout(template="plotly_dark")
vis.show()
```


<div>                            <div id="03e4c10a-e124-42f9-876d-a567f81b1606" class="plotly-graph-div" style="height:650px; width:650px;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("03e4c10a-e124-42f9-876d-a567f81b1606")) {                    Plotly.newPlot(                        "03e4c10a-e124-42f9-876d-a567f81b1606",                        [{"domain":{"x":[0.0,1.0],"y":[0.0,1.0]},"hovertemplate":"label=%{label}\u003cbr\u003evalue=%{value}\u003cextra\u003e\u003c\u002fextra\u003e","labels":["Kolkata","Mumbai","Chennai","Pune","Hyderabad","Bangalore","Ahmedabad","Delhi","Surat"],"legendgroup":"","name":"","showlegend":true,"values":[1346,1277,1106,1090,1075,946,717,611,512],"type":"pie"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"legend":{"tracegroupgap":0},"title":{"text":"Top 10 Cities Ordering Food from Swiggy"},"height":650,"width":650},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('03e4c10a-e124-42f9-876d-a567f81b1606');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>



```python
#Heat Map
```


```python
numeric_df = df.select_dtypes(include=[np.number])
correlation_matrix = numeric_df.corr()
fig = go.Figure(data=go.Heatmap(z=correlation_matrix, x=correlation_matrix.columns, y=correlation_matrix.columns,colorscale='Viridis') )
fig.update_layout(title='Correlation Heatmap of Factors Affecting Average Rating')
fig.show()
```


<div>                            <div id="75da00e0-ed3a-4ebe-b7ec-f33f42b071cc" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("75da00e0-ed3a-4ebe-b7ec-f33f42b071cc")) {                    Plotly.newPlot(                        "75da00e0-ed3a-4ebe-b7ec-f33f42b071cc",                        [{"colorscale":[[0.0,"#440154"],[0.1111111111111111,"#482878"],[0.2222222222222222,"#3e4989"],[0.3333333333333333,"#31688e"],[0.4444444444444444,"#26828e"],[0.5555555555555556,"#1f9e89"],[0.6666666666666666,"#35b779"],[0.7777777777777778,"#6ece58"],[0.8888888888888888,"#b5de2b"],[1.0,"#fde725"]],"x":["ID","Price","Avg ratings","Total ratings","Delivery time"],"y":["ID","Price","Avg ratings","Total ratings","Delivery time"],"z":[[1.0,-0.14408557087833204,-0.4579584290007433,-0.18914921770100132,0.14381665483628506],[-0.14408557087833204,1.0,0.11363038630435658,-0.014671890656569257,0.07600855580829947],[-0.4579584290007433,0.11363038630435658,1.0,0.15790032898975895,-0.1469869356888259],[-0.18914921770100132,-0.014671890656569257,0.15790032898975895,1.0,-0.08408979863896718],[0.14381665483628506,0.07600855580829947,-0.1469869356888259,-0.08408979863896718,1.0]],"type":"heatmap"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"title":{"text":"Correlation Heatmap of Factors Affecting Average Rating"}},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('75da00e0-ed3a-4ebe-b7ec-f33f42b071cc');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>



```python

```


```python

```
