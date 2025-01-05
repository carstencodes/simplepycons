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


class ImprovmxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "improvmx"

    @property
    def original_file_name(self) -> "str":
        return "improvmx.svg"

    @property
    def title(self) -> "str":
        return "ImprovMX"

    @property
    def primary_color(self) -> "str":
        return "#2FBEFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ImprovMX</title>
     <path d="M12.043 7.203 7.326 9.757 7.309
 4.75h1.66l6.13-.026h1.66l.009 4.998zm1.72-5.875.008
 2.077-3.482.009V1.337h3.473zm4.341 9.11-.025-7.041h-2.98L15.09 0
 8.96.017v3.405H5.98l.018 7.041-2.767 1.499.92 3.32a5.79 5.79 0 0 1
 1.387.068l-.75-2.724 6.59-3.559.018 8.548h1.328l-.026-8.548 6.615
 3.525-.715 2.656a5.79 5.79 0 0 1
 1.345.085l.937-3.414-2.784-1.481zm-2.81 7.654a4.623 4.623 0 0 1-6.58
 0 5.951 5.951 0 0 0-8.403 0l.91.91a4.657 4.657 0 0 1 6.582 0A5.9 5.9
 0 0 0 12 20.748a5.9 5.9 0 0 0 4.197-1.746 4.657 4.657 0 0 1 6.581
 0l.911-.91a5.951 5.951 0 0 0-8.403 0m.009 3.252a4.623 4.623 0 0
 1-6.581 0 5.874 5.874 0 0 0-3.346-1.652v1.286c.885.17 1.745.596 2.435
 1.277A5.9 5.9 0 0 0 12 24a5.9 5.9 0 0 0 4.197-1.745 4.614 4.614 0 0 1
 2.299-1.243v-1.303a5.91 5.91 0 0 0-3.21 1.635" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

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
