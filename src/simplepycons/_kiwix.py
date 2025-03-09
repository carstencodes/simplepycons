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


class KiwixIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "kiwix"

    @property
    def original_file_name(self) -> "str":
        return "kiwix.svg"

    @property
    def title(self) -> "str":
        return "Kiwix"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Kiwix</title>
     <path d="M23.968 15.033c-.185-.811-1.527-3.15-4.27-5.224a27.047
 27.047 0 0 0-1.33-.95c.548-2.346-2.303-5.177-5.084-3.844C11.287 3.136
 9.06 2.37 7.012 2.401c-5.422.076-9.605 5.725-5.106
 11.117l.01.009c.068.082.14.165.211.247.292.35.486.66.65 1.206l1.343
 4.397h-.475a.794.794 0 0 0-.794.794h1.801L7.68 21.6a.79.79 0 0
 0-.377-1.054l-.793-.374H8.79a.794.794 0 0 0-.793-.794H5.929a.822.822
 0 0 1-.786-.581L4.08
 15.305c-.266-.918.343-1.517.915-1.589.522-.064.785.272 1.03
 1.088l.945 3.098h-.475a.794.794 0 0 0-.793.793h1.8l3.027 1.431a.79.79
 0 0 0-.376-1.054l-.794-.375h1.674a4 4 0 0 0 6.278.805 4 4 0 0 0
 0-5.654 4 4 0 0 0-6.632 4.056H8.784a.822.822 0 0
 1-.787-.582l-1.569-5.157.268-.142c3.724-1.563 7.707 1.228
 10.479-1.454l.018-.017c.343-.312.686-.631 1.7.004 1.092.684 3.501
 2.47 4.593 5.522.002 0 .665-.236.482-1.045zm-7.662-6.764a.769.769 0 1
 0-1.275.595 1.2 1.2 0 1 1 1.275-.595z" />
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
