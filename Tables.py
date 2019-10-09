import plotly.graph_objects as go

fig1 = go.Figure(data=[go.Table(header=dict(values=['Coding','Programming'],
                                            line_color="red",
                                            fill_color="lightskyblue",
                                            ),
                                cells=dict(values=[['Process of writing codes from one language to another\n',
                                                    'Primary aim of coding is to initiate communication between human and machines\n'],
                                                   ['Process of creating an executable machine program which performs set of instructions\n',
                                                    'Formally writing codes so that human inputs and machine outputs remain sync\n']],
                                           line_color="orange",
                                           fill_color="white"))])


fig1.write_html('Tables.html', auto_open=True)
#fig1.show()
