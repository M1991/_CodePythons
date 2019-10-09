Sub DateFilter_1()
'
' DateFilter_1 Macro
'
Dim asdate As ActiveCell.Formula
'
    ActiveWindow.SmallScroll Down:=-12
    Selection.AutoFilter
    ActiveSheet.Range("$A$1:$K$278").AutoFilter Field:=2, Criteria1:= _
        "19/09/2019"
    ActiveSheet.Range("$A$1:$K$278").AutoFilter Field:=7, Criteria1:= _
        "XPRESS CREDIT"
End Sub
----------------------------------------------------------------------------------
Sub DateMacro()
'
' DateMacro Macro
'

'
    ActiveCell.FormulaR1C1 = "9/23/2019"
    Range("U6").Select
End Sub
----------------------------------------------------------------------------------
Sub MacroDataCopy()
'
' MacroDataCopy Macro
'

'
    Range("G48").Select
    Selection.Copy
    Windows("13339.xlsx").Activate
    ActiveWindow.SmallScroll Down:=15
    Range("B31").Select
    ActiveSheet.Paste
    Windows("114504.xlsx").Activate
End Sub
----------------------------------------------------------------------------------
Sub SumMacro()
'
' SumMacro Macro
'

'
    Range("L165").Select
    Application.CutCopyMode = False
    ActiveCell.FormulaR1C1 = "=SUM(R[-117]C[-4]:R[2]C[-4])"
    ActiveCell.FormulaR1C1 = "=SUM(R[-117]C[-3]:R[2]C[-3])"
    Range("M165").Select
End Sub
----------------------------------------------------------------------------------
Sub SumMacro2()
'
' SumMacro2 Macro
'

'
    Application.CutCopyMode = False
    ActiveCell.FormulaR1C1 = "=SUM(R[-119]C[-3]:RC[-3])"
    Range("M167").Select
End Sub
Sub EditNewMacro()
'
' EditNewMacro Macro
'

'
    Selection.Copy
    Sheets("SEPTEMBER").Select
    ActiveSheet.Range("$A$1:$K$278").AutoFilter Field:=2, Criteria1:=Array( _
        "19/09/2019"), Operator:=xlFilterValues, Criteria2:=Array(1, "9/9/2019")
End Sub
