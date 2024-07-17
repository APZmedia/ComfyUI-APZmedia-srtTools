import re

def srt_to_prose(srt_file):
    """
    Convert an SRT file to prose by stripping timestamps and formatting.
    
    Parameters:
    srt_file (str): Path to the SRT file.
    
    Returns:
    str: Prose content of the SRT file.
    """
    with open(srt_file, 'r', encoding='utf-8') as file:
        srt_content = file.read()
    
    # Remove timestamps and subtitle indexes
    srt_content = re.sub(r'\d+\n', '', srt_content)
    srt_content = re.sub(r'\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}', '', srt_content)
    
    # Remove extra newlines and convert to prose
    prose_content = re.sub(r'\n+', ' ', srt_content).strip()
    
    return prose_content

# Example usage
srt_file_path = 'path_to_your_srt_file.srt'
prose_content = srt_to_prose(srt_file_path)
print(prose_content)

# If you want to save the prose content to a file
with open('prose_output.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(prose_content)
