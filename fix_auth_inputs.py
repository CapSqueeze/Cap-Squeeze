import os

files_to_fix = ['login.html', 'signup.html']

for file in files_to_fix:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the CSS rule for .form-input to ensure padding is respected
    old_rule = 'padding: 15px 20px 15px 45px;'
    new_rule = 'padding: 15px 20px 15px 45px !important; box-sizing: border-box !important;'
    
    if old_rule in content:
        content = content.replace(old_rule, new_rule)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {file}")
    else:
        print(f"Could not find old rule in {file}")
