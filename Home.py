import streamlit as st

uploaded_file = st.file_uploader(
    "Choose your database", accept_multiple_files=False)
if uploaded_file is not None:
    file_name = uploaded_file
else:
    file_name = "DatabaseSample.xlsx"


st.title('IMDB Movies Data Analysis')
st.markdown('This App is Analysis for Top movies on IMDB')

st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAkFBMVEX1xRgAAAD+zBn5yBhpVQrGnxPgtBb4xxiRdA5QQAgOCwGtixFTQwj8yxnTqhWMcQ7rvRd0XQu1khE5LgZmUgphTgnLoxQyKAU7LwaHbA1IOgeXeQ//0xrwwRjmuRfBmxNENwajgxAYEwJ+ZQzQpxS6lhJ3Xwyefw+ohxAsIwQdGANcSgkhGwOwjhGCaQ0nHwR6R0fmAAAEu0lEQVR4nO2b6XqqOhhGTaLEtjvWobZ1ALTa+dje/90diRXIoJvsAFKed/3CJMK3GBIy0OkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADABaAaTKYKPTlBHP9zJpfZso4lBOPKsfX9iE4FRJ9dhekuURSzu67B3ehg3+FmXkISH4un9kzJ1zr4OYMHQf0oU2YL0Q8eEI3bJFA615MlP38KrZmEJoY39ryUhzFNryO90nMruIimYV9Yjy0ZyOD4wJp5XciQkNXweKXon8YZPsvYWOxlSEjAGmu4kBGwtachCXlTDUcyAjHzNfxDm2q4kpHRqa8hiVlDDcnB8MHbcE6bajhMHiBqz3MxJBFvqGHSXPCoBENZKzfRcMxONoduhq+ioYZJc8GenQxv4p2l7u031fBlnylenQwHgtHwSU+9baphUgeKjZvh/tEVb7/G8InZ4vqrIbv/NYYk3Oe9Oxue6sGcMOQsgZ+LuzrDJN4TWecMhw6GjEbxbv02HnBahqSr4Zidag7PGXaKGzL2Njn+GgW0fsOFMJ+pMg1pT6l2N9z7MroadgUbV2i41Fuih9BX0dVwRcWiQsO1sddvT0FnQ0LFKN3+KN3Qwp3ns1jM8OM63YxyWepwVUWGpOc3AFfMcJU1gdtluvl+V4vh3O8iFjTMevW7rHd41a3FkARelU1Bw6x30M+aw01Nhjdet2kxw8cs7tE23VxUYPj59WmkzbzeVosZTrJWfpX1Dp/Lfw4jKqgR0Usdhtmt+XSbxV6+YbIL2tUSRzUYPuQGn7KohuqoYjnvpfvOpP5KUYvh8kMvtmdZjaExpF6Pofn8k/+qMtxdxPDLNPysylB/ta/HcG0afrXKkPZMw9d2GRrFCIlpqwwtE9uDdhnSb8MwbJPhhJpzhk+sXYbmvO9Kt/7lhswYlx+JlhkazUW/ZYZmuTGj5fctLmhoTm1vedsM9fmYqHWGenOxT2qXobhVi727GJqzOQ001EOfOhm6zB9ezFCbcpoJB0OnOeBLGeo32htzMTSWbzStjz9JgleL9VwMRd/FUH99qsuQTpSkgBc35ObU/7mxNn0OsS5DoQ5jJoUKGQaUBvoI6HlDrdauz1A58Lcwhm5PGM5X13oS+VmLaxkRZowtVxcwfKR6BXBFixraWdtX7s3H29joiW5qMuTbfMqm8DW0c283tNKvy1BpLpK7THgYyoMXNIzrmF2TMyb5lGR9qIfhy4k1wlZCH0Enw3wNIFu5fzeUS4QLGo7qmOWWhorQUE9wMjx81VDQMPJbUeNimJ/1MpRdDI8LSAzDiWWN/NqrnnEyzL8RT3wM0/bNMNyYa+ZefJe2ORjmmwv5ndo/Gt6kMRuGYxpoq4ln3mv3TvXc1PeKd3mcUCsktLZZGhqjjiqPr53srjO+kIs46+Tn8b57JSxODOOeily9wrdK2v3hYU9/x4dCA/WfTJ4xfX95tqHyEaV2lF5PfoQRLX5ObzcWpXyPyDQOMtyS1jlfiNnSbPvOKWr5h0RBxTCI9iejgu8tm4P/ulIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAZ/kfV59xgQ6j6wsAAAAASUVORK5CYII=' , width=200)

st.header('Description')
st.write('''This App is for Top 1000 movis as rated by regular IMDB voters and Critics''')
st.header('What is IMDB ?')
st.write('''IMDB is an online database of information related to films,
          television series, podcasts, home videos, video games, 
         and streaming content online – including cast, 
         production crew and personal biographies, 
         plot summaries, trivia, ratings, 
         and fan and critical reviews.''')
