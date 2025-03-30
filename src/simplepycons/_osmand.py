#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class OsmandIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "osmand"

    @property
    def original_file_name(self) -> "str":
        return "osmand.svg"

    @property
    def title(self) -> "str":
        return "OsmAnd"

    @property
    def primary_color(self) -> "str":
        return "#FF8800"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>OsmAnd</title>
     <path d="M12 0C6.11 0 1.332 4.777 1.332 10.668a10.67 10.67 0 0 0
 6.52 9.828c1.927.836 2.667 1.282 3.26
 2.467q.085.172.152.326c.189.422.318.711.736.711s.546-.289.736-.71q.069-.155.153-.327c.593-1.186
 1.28-1.63 3.26-2.467a10.67 10.67 0 0 0 6.519-9.828C22.668 4.777 17.89
 0 12 0m-.443 4.758a5.926 5.926 0 0 1 6.369 5.91 5.926 5.926 0 0
 1-11.852 0 5.926 5.926 0 0 1 5.483-5.91" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/osmandapp/OsmAnd-misc/blob
/9ec3bacebf580d0862ded5813a4aa934d0862302/logo/osmand/symbol_osmand.sv'''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
