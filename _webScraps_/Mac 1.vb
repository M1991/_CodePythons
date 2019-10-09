Sub NewMacroOrg()
	'Dim actCell as Acti
	Dim cel as Range
	Dim sumvar as Long
	Selection.Copy
    Sheets("SEPTEMBER").Select
    ActiveSheet.Range("$A$1:$K$278").AutoFilter Field:=2, Criteria1:=Array( _
        "19/09/2019"), Operator:=xlFilterValues, Criteria2:=Array(1, "9/9/2019")
    
	
	 ActiveCell.FormulaR1C1 = "=SUM(R[-119]C[-3]:RC[-3])"
	' Filter code	
	' Count Sum and Count
	'
	'
	
	 
	 
	 
	 
End Sub

Sub NewmacroWork()
    lastrow = Worksheets("Sheet5").Cells(Rows.Count, 5).End(xlUp).Row
    Dim a As Long
    a = 0
    MsgBox (lastrow)
    For i = lastrow To 2 Step by - 1
    
    a = a + Worksheets("Sheet5").Cells(i, 5).Value
    
    Next
    
    Worksheets("Sheet5").Cells(lastrow + 1).Value = a

End Sub




Sub NewmacroWork()
    Dim ws As Worksheet
    Dim rng As Range
    Dim lastcol As Long

    Set ws = ThisWorkbook.Sheets("SEPTEMBER")
    Set rng = ws.Range("$A$1:$K$258")

    ws.AutoFilterMode = False
    rng.AutoFilter Field:=2, Criteria1:=Array("9/09/2019"), Operator:=xlFilterValues, Criteria2:=Array(1, "9/9/2019")
    rng.AutoFilter Field:=7, Criteria1:="XPRESS CREDIT"
    
    lastcol = Application.WorksheetFunction.Sum(rng.SpecialCells(xlCellTypeVisible))


    'LastRow = Worksheets("Sheet5").Cells(Rows.Count, 5).End(xlUp).Row
    'lastcol = Worksheets("SEPTEMBER").Cells(Rows.Count, 1).End(xlUp).Row   
    
    Dim a As Integer
    a = 0
    
    MsgBox (lastcol)   


End Sub