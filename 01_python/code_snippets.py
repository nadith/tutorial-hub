    # Code snippets to use
    
    def __repr__(self) -> str:
        if self.ref is not None:
            summary = f"ref: {self.ref}/{self.path}"
        else:
            summary = "digest: %s" % self.digest

        return "<ManifestEntry %s>" % summary
    
    
    
name = 'Damith' or None => 'Damith'
name = None or 'Damith' => 'Damith'
name = 'Damith' or 'Nadith' => 'Damith'
name = None or None => None