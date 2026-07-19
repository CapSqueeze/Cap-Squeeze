def fix_mojibake(text):
    try:
        return text.encode('windows-1252').decode('utf-8')
    except:
        return text

test_str = "â‚¹799 and Best Seller ðŸ † and â€”"
print(fix_mojibake(test_str))
