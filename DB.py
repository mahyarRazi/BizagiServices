
import pyodbc
from fpdf import FPDF

# GIG
conn_gig =pyodbc.connect('Driver={SQL Server};' 'Server=GIG-DC1-P451;' 'Database=MicrosoftDynamicsAX_Operatinal;'
                     'persist security info=True;  Integrated Security=SSPI;')


curser=conn_gig.cursor()
df = curser.execute('select top 5 *from [MassStoring].[VW_ItemlocationOrder]')
print (df.tables()0])
conn_gig.commit();








