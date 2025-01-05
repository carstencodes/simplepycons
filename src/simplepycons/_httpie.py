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


class HttpieIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "httpie"

    @property
    def original_file_name(self) -> "str":
        return "httpie.svg"

    @property
    def title(self) -> "str":
        return "HTTPie"

    @property
    def primary_color(self) -> "str":
        return "#73DC8C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>HTTPie</title>
     <path d="M7.28 0C4.4 0 1.992 2.279 1.933 5.155a5.263 5.263 0 0 0
 5.26 5.358h4.223a.306.306 0 0 1 .122.584l-6.47 2.835a5.263 5.263 0 0
 0-3.135 4.85C1.953 21.683 4.368 24 7.273 24h2.212c2.922 0 5.357-2.345
 5.35-5.267a5.263 5.263 0 0 0-3.29-4.867.303.303 0 0
 1-.007-.556l7.402-3.246a5.263 5.263 0 0 0 3.128-4.846C22.047 2.317
 19.626.003 16.724.003z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/httpie/httpie/blob/d262181'''

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
