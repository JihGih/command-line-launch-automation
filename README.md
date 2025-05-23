## Hello
"lancer des commandes cmd" is a Python script that allows you to execute system commands from a JSON file. It uses the `subprocess` module to run the commands and captures their output.
## Prerequisites
- Python 3.x
- `pip install PyInstaller`
## Usage
1. Create a JSON file named `commande.json` in the `data` directory. For example:
```json
{
    "project_name": {
        "path": "C:/laragon/www/my_laravel_project",
        "commande": ["php artisan reverb:start", "php artisan queue:work", "no_shell\"C:/Program Files/Git/git-bash.exe\""]
    },
}
```
2. Run the script using Python:
```bash
python main.py
```
3. The script will read the commands from the JSON file and execute them one by one. The output of each command will be printed to the console.

4. To build the script into a standalone executable, use PyInstaller:
```bash
python -m PyInstaller --onefile --add-data "data/commande.json;data" main.py
```
5. After building, you can find the executable in the `dist` directory. You can run it directly without needing Python installed on the system.
## Example JSON File
```json
{
    "project_name": {
        "path": "C:/laragon/www/my_laravel_project",
        "commande": ["php artisan reverb:start", "php artisan queue:work", "no_shell\"C:/Program Files/Git/git-bash.exe\""]
    },
}
```
## Example Output
```
C:\laragon\www\my_laravel_project>php artisan reverb:start
Laravel development server started: <http://
C:\laragon\www\my_laravel_project>php artisan queue:work
Laravel development server started: <http://
C:\laragon\www\my_laravel_project>"C:/Program Files/Git/git-bash.exe"
```

## Note
- Make sure to adjust the commands in the JSON file according to your operating system and requirements.
- The script captures both standard output and standard error, so any errors will also be printed to the console.
- The script uses `shell=True` in the `subprocess.run()` function, which is generally not recommended for security reasons. Be cautious when using this option, especially with user-generated input.
- The script is designed to work on Windows. If you are using a different operating system, you may need to modify the commands in the JSON file accordingly.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author
- Jih Giarjah RAZAFIMAHALEO
- [GitHub](https://github.com/JihGih)
- [LinkedIn](https://www.linkedin.com/in/jih-giarjah-razafimahaleo-233510310)
- [Portfolio](https://giarjah.vercel.app)
- [Email](mailto:giarjah@gmail.com)