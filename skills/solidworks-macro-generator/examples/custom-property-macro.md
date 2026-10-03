# Example: write a material property to Custom Properties

Task: read the active model's material-related information and write a project property.

Safe design:
1. Confirm the active document is the expected Part/Assembly type.
2. Read the available material information using a version-appropriate API path.
3. Handle missing material information explicitly.
4. Write to a named Custom Property.
5. Report success/failure instead of assuming the write succeeded.
6. Test on a copy before batch use.

The macro answer must flag any API member whose exact availability has not been verified for the user's SolidWorks version.
