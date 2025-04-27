## Baby Keygen
I didn't strip this one you're welcome

Flag Format: CIT{example_flag}

## Solution

Opening up the binary in BinaryNinja, I navigate to the main function:

```c
00407ff5    int64_t main()

00407ffe        void* fsbase
00407ffe        int64_t rax = *(fsbase + 0x28)
00408014        std::string::string()
0040802d        std::operator<<<std::char_traits<char> >(&std::cout, "Enter key: ")
00408043        void var_68
00408043        std::getline<char>(&std::cin, &var_68)
00408056        void var_48
00408056        std::string::string(&var_48, &var_68, &var_68)
00408062        check_key(&var_48)
0040806e        std::string::~string(&var_48)
0040807f        std::string::~string(&var_68)
0040807f        
00408093        if (rax == *(fsbase + 0x28))
004080e0            return 0
004080e0        
004080d6        return __stack_chk_fail()
```

What I can gather from this function is that I need to navigate to the check_key function to figure out how keygen works.

check_key:
```c
00407e8a        int64_t var_60 = arg1
00407e8e        void* fsbase
00407e8e        int64_t rax = *(fsbase + 0x28)
00407ead        int64_t rax_2
00407ead        rax_2.b = std::string::length(var_60) != 0x10
00407eb2        int64_t result
00407eb2        
00407eb2        if (rax_2.b == 0)
00407ed3            void var_48
00407ed3            std::string::substr(&var_48, var_60, 0, 4)
00407ee9            char rax_3 = std::operator!=<char>(&var_48, "KEY_", "KEY_")
00407ef7            std::string::~string(&var_48)
00407ef7            
00407efe            if (rax_3 == 0)
00407f07                int64_t var_50_1 = 4
00407f07                
00407f4b                while (true)
00407f4b                    if (var_50_1 u> 0xf)
00407f5b                        std::string::string(&var_48, var_60)
00407f67                        validate(&var_48)
00407f73                        std::string::~string(&var_48)
00407f78                        result = 0
00407f78                        break
00407f78                    
00407f33                    int32_t rax_8
00407f33                    rax_8.b =
00407f33                        isalnum(zx.q(sx.d(*std::string::operator[](var_60, var_50_1)))) == 0
00407f33                    
00407f38                    if (rax_8.b != 0)
00407f3a                        result = 0
00407f3f                        break
00407f3f                    
00407f41                    var_50_1 += 1
00407efe            else
00407f00                result = 0
00407eb2        else
00407eb4            result = 0
00407eb4        
00407f8a        if (rax == *(fsbase + 0x28))
00407ff4            return result
00407ff4        
00407fea        return __stack_chk_fail()
```

This function checks if the input is exactly 16 charecters long, starts with "KEY_", and that charecters 5-16 are alphanumerical. If the input passes all these conditions, the flag is given. A input that fits these conditions is `KEY_ABCDEFGHIJKL`

```bash
┌──(dev㉿dev)-[~/Downloads]
└─$ ./babykeygen
Enter key: KEY_ABCDEFGHIJKL
CIT{41jN8BKzz388}
```

FLAG: `CIT{41jN8BKzz388}`
