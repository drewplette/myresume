document.addEventListener('DOMContentLoaded', function() {
    const portfolioItems = document.querySelectorAll('.portfolio-item');
    const filterInput = document.getElementById('filter-input');
    const filterTags = document.querySelectorAll('.filter-tag');
    
    // Add click event to each portfolio item for expanding/collapsing
    portfolioItems.forEach(item => {
        item.addEventListener('click', function(e) {
            // If clicking on a link inside an expanded item, don't toggle
            if (this.classList.contains('expanded') && 
                (e.target.tagName === 'A' || e.target.closest('a'))) {
                return;
            }
            
            // Check if any item is already expanded
            const expandedItem = document.querySelector('.portfolio-item.expanded');
            
            // If clicking on an already expanded item, collapse it
            if (this.classList.contains('expanded')) {
                this.classList.remove('expanded');
                
                // Scroll to the top of the item after collapse
                setTimeout(() => {
                    this.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                }, 100);
            } 
            // If clicking on a collapsed item
            else {
                // If another item is expanded, collapse it first
                if (expandedItem) {
                    expandedItem.classList.remove('expanded');
                }
                
                // Expand this item
                this.classList.add('expanded');
                
                // Scroll to the expanded item
                setTimeout(() => {
                    this.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                }, 100);
            }
        });
    });
    
    // Filter functionality
    filterInput.addEventListener('input', filterProjects);
    
    // Filter tag buttons
    filterTags.forEach(tag => {
        tag.addEventListener('click', function() {
            // Remove active class from all tags
            filterTags.forEach(t => t.classList.remove('active'));
            
            // Add active class to clicked tag
            this.classList.add('active');
            
            // Clear text input when using tag filters
            if (filterInput.value) {
                filterInput.value = '';
            }
            
            filterProjects();
        });
    });
    
    // Function to filter projects
    function filterProjects() {
        const searchTerm = filterInput.value.toLowerCase();
        const activeTag = document.querySelector('.filter-tag.active');
        const tagFilter = activeTag ? activeTag.dataset.tag : 'All';
        
        portfolioItems.forEach(item => {
            const itemText = item.textContent.toLowerCase();
            const itemTags = item.dataset.tags ? item.dataset.tags.split(',') : [];
            
            // Check if item matches search term
            const matchesSearch = searchTerm === '' || itemText.includes(searchTerm);
            
            // Check if item matches tag filter
            const matchesTag = tagFilter === 'All' || itemTags.some(tag => 
                tag.toLowerCase() === tagFilter.toLowerCase());
            
            // Show/hide based on both filters
            if (matchesSearch && matchesTag) {
                item.classList.remove('hidden');
            } else {
                item.classList.add('hidden');
                
                // If a hidden item was expanded, collapse it
                if (item.classList.contains('expanded')) {
                    item.classList.remove('expanded');
                }
            }
        });
    }
    
    // Close expanded item when clicking outside
    document.addEventListener('click', function(e) {
        if (!e.target.closest('.portfolio-item') && !e.target.closest('.filter-bar')) {
            const expandedItem = document.querySelector('.portfolio-item.expanded');
            if (expandedItem) {
                expandedItem.classList.remove('expanded');
            }
        }
    });
});