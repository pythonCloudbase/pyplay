A python program to create yara rules from text file

initial output: 

```
PS C:\codeplay\pyplay\yara_rules_creator> python .\yara_creator.py
Enter the method you want to provide input 
                        (1 : for text)
                        (2 : for manual input)
                        :> 1
TPConnSvc.dll


rule TPConnSvc.dll

{
    strings:
        $text = TTKP.DAT


    condition:
        $text

}
```