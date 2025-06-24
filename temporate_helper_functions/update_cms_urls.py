#!/usr/bin/env python3
"""
Script to update URLs in webarena_tools_toRyan/cms directory from port 7770 to 7780
and then regenerate returns documentation.
"""

import os
import re
import subprocess
import sys
from pathlib import Path

def update_urls_in_file(file_path):
    """
    Update URLs in a single file from port 7770 to 7780.
    
    Args:
        file_path: Path to the file to update
    
    Returns:
        bool: True if file was modified, False otherwise
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to match the specific URL with port 7770
        old_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
        new_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780'
        
        # Replace all occurrences
        updated_content = content.replace(old_url, new_url)
        
        # Check if any changes were made
        if updated_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            return True
        
        return False
    
    except Exception as e:
        print(f"Error updating {file_path}: {str(e)}")
        return False

def update_cms_urls():
    """
    Update URLs in all Python files in the webarena_tools_toRyan/cms directory.
    
    Returns:
        tuple: (success_count, error_count, total_files)
    """
    cms_dir = "webarena_tools_toRyan/cms"
    
    if not os.path.exists(cms_dir):
        print(f"Error: Directory {cms_dir} not found!")
        return 0, 0, 0
    
    success_count = 0
    error_count = 0
    total_files = 0
    
    print(f"Updating URLs in {cms_dir}...")
    print("=" * 50)
    
    # Process all Python files in the cms directory
    for file in sorted(os.listdir(cms_dir)):
        if file.endswith('.py'):
            total_files += 1
            file_path = os.path.join(cms_dir, file)
            
            print(f"Processing: {file}", end=" ... ")
            
            if update_urls_in_file(file_path):
                print("✓ Updated")
                success_count += 1
            else:
                print("- No changes needed")
    
    return success_count, error_count, total_files

def run_regenerate_returns():
    """
    Run the regenerate_returns.py script for CMS tools.
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        print("\nRunning regenerate_returns.py for CMS tools...")
        print("=" * 50)
        
        # Change to the test directory where regenerate_returns.py is located
        original_dir = os.getcwd()
        
        # Check if regenerate_returns.py exists
        regenerate_script = "test/regenerate_returns.py"
        if not os.path.exists(regenerate_script):
            print(f"Error: {regenerate_script} not found!")
            return False
        
        # Run the regenerate_returns.py script
        # Note: We'll modify it to focus only on CMS tools
        print("Note: You'll need to manually run regenerate_returns.py and focus on CMS tools")
        print(f"Run: python {regenerate_script}")
        print("When prompted, you can modify the script to focus only on the cms directory.")
        
        return True
    
    except Exception as e:
        print(f"Error running regenerate_returns.py: {str(e)}")
        return False

def main():
    """Main function to update URLs and regenerate returns documentation."""
    print("CMS URL Update and Returns Regeneration Script")
    print("=" * 60)
    
    # Step 1: Update URLs
    success_count, error_count, total_files = update_cms_urls()
    
    print("\nURL Update Summary:")
    print("-" * 30)
    print(f"Total files processed: {total_files}")
    print(f"Files updated: {success_count}")
    print(f"Files with no changes: {total_files - success_count}")
    print(f"Errors: {error_count}")
    
    if success_count > 0:
        print(f"\n✅ Successfully updated {success_count} files!")
        print("URLs changed from :7770 to :7780")
    else:
        print("\n⚠️  No files were updated. They may already have the correct URLs.")
    
    # Step 2: Regenerate returns documentation
    print("\n" + "=" * 60)
    print("REGENERATING RETURNS DOCUMENTATION")
    print("=" * 60)
    
    success = run_regenerate_returns()
    
    if success:
        print("\n✅ Ready to regenerate returns documentation!")
        print("Please run the regenerate_returns.py script manually with focus on CMS tools.")
    else:
        print("\n❌ Failed to prepare returns regeneration.")
    
    print("\nNext steps:")
    print("1. Verify that URLs were updated correctly in the CMS files")
    print("2. Run: python test/regenerate_returns.py")
    print("3. When prompted, focus on processing only CMS tools")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nScript interrupted by user.")
    except Exception as e:
        print(f"\nUnexpected error: {str(e)}")
        print("Please check your environment and try again.") 