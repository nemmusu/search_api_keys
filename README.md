
# Search for API Keys in AndroidManifest.xml

This Python script scans (recursively in a folder or a single file) for API keys in the `<meta-data>` tag within `AndroidManifest.xml` files.

## How It Works

1. **Recursive Search**: When a folder is specified (`-d` or `--directory`), the script scans all subfolders for `AndroidManifest.xml` files and analyzes them.
2. **Single File Search**: When a specific file is specified (`-f` or `--file`), the script only checks that file.
3. **Regex**: Extracts the attributes `android:name` and `android:value` from `<meta-data>` tags where `android:name` contains `API_KEY` in any format.

## Installation

- Clone or download this repository
- Ensure you have Python 3 installed

Example of quick installation in a local folder:

```bash
git clone https://github.com/nemmusu/search_api_keys.git
cd search_api_keys
```

## Usage

```bash
python search_api_keys.py -d /path/to/folder
```

or

```bash
python search_api_keys.py -f /path/to/single/AndroidManifest.xml
```

Where:
- `-d, --directory` specifies the folder to scan recursively
- `-f, --file` specifies a single `AndroidManifest.xml` file to check

### Example Output

Suppose you have an `AndroidManifest.xml` file with:
```xml
<meta-data
    android:name="com.google.android.maps.v2.API_KEY"
    android:value="XXXXXX_API_KEY_XXXXXXXX" />
```

Might produce the following output:
```
[FOUND][API-KEY] /home/user/project/AndroidManifest.xml - line 812 => Name: com.google.android.maps.v2.API_KEY | Value: XXXXXX_API_KEY_XXXXXXXX
```


