# Fail before writing if two pages would silently overwrite the same URL.
Jekyll::Hooks.register :site, :post_render do |site|
  documents = site.collections.values.select { |collection| collection.metadata['output'] }
                  .flat_map(&:docs)
  destinations = {}
  (site.pages + documents + site.static_files).each do |item|
    next if item.respond_to?(:data) && item.data['published'] == false

    destination = item.destination(site.dest)
    if destinations.key?(destination)
      raise Jekyll::Errors::FatalException,
            "Duplicate output #{destination}: #{destinations[destination]} and #{item.path}"
    end
    destinations[destination] = item.path
  end
end
