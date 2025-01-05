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


class PubmedIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pubmed"

    @property
    def original_file_name(self) -> "str":
        return "pubmed.svg"

    @property
    def title(self) -> "str":
        return "PubMed"

    @property
    def primary_color(self) -> "str":
        return "#326599"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>PubMed</title>
     <path d="M8.23 7.982l.006-1.005C7.846 1.417 5.096 0 5.096 0l.048
 2.291C3.73 1.056 2.6 1.444 2.6 1.444l.118 15.307s4.218-1.796 5.428
 5.505C10.238 13.535 21.401 24 21.401 24V9S10.52-.18 8.231 7.982zm9.79
 9.941l-1.046-5.232-1.904 4.507h-.96l-1.72-4.301-1.046
 5.04H9.321l2.093-9.39h.802l2.491 5.543 2.508-5.557h.869l2.075
 9.39h-2.138z" />
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
