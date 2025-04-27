function calculate(num1,num2,operator)
    if operator == "+" then
        return num1 + num2
    elseif operator == "-" then
        return num1 - num2
    elseif operator == "*" then
        return num1 * num2
    elseif operator == "/" then
        if num2 == 0 then
            return "Error: Division by zero is not allowed."
        else
            return num1 / num2
        end
    else
        return "Error: Invalid operator."
    end
end

io.write("Enter the first number: ")
local input1 = io.read()
local number1 = tonumber(input1)
if not number1 then
    print("Invalid input. Please enter a valid number.")
    os.exit(1)
end

io.write("Enter an operator (+, -, *, /): ")
local operator = io.read()

io.write("Enter the second number: ")
local input2 = io.read()
local number2 = tonumber(input2)
if not number2 then
    print("Invalid input. Please enter a valid number.")
    os.exit(1)
end

local result = calculate(number1, number2, operator)

print("Result: " .. tostring(result))







































   	    		
	
     	  	  	
	
     	 	 	  
	
     				 		
	
     		 	   
	
     		  		 
	
     			 	  
	
      		 	  
	
     		   	 
	
     	 	 	  
	
      		    
	
      		 	  
	
      		   	
	
      		 	 	
	
     	  		  
	
     		   	 
	
     					 	
	
  




-- nope no flag here, keep looking :P