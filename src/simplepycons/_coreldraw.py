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


class CoreldrawIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "coreldraw"

    @property
    def original_file_name(self) -> "str":
        return "coreldraw.svg"

    @property
    def title(self) -> "str":
        return "CorelDRAW"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>CorelDRAW</title>
     <path d="M10.651 0C10.265.019 9.4.272 8.584.657c-.816.39-3.696
 2.161-3.752 6.536.072 4.145 3.847 11.191 6.397 13.455 0
 0-4.141-6.952-4.439-13.013C6.488 1.575 10.651 0 10.651 0Zm2.679
 0s4.159 1.575 3.861 7.635c-.299 6.061-4.439 13.013-4.439 13.013
 2.547-2.264 6.324-9.31
 6.396-13.455-.057-4.375-2.936-6.146-3.752-6.536C14.58.272 13.715.019
 13.33 0Zm-1.38.019a1.088 1.088 0 0 0-.555.144C9.864.99 8.909 3.982
 9.177 8.66c.185 3.242 1.009 7.291 2.422 11.988h.7c1.413-4.697
 2.24-8.742 2.425-11.984.268-4.677-.688-7.674-2.219-8.501a1.088 1.088
 0 0 0-.555-.144ZM7.017 1.066S2.543 2.909 3.431 8.225c.884 5.32 5.588
 10.995 6.986 12.2.503.457-5.777-6.548-6.386-12.699-.291-2.323.39-4.9
 2.986-6.66Zm9.966 0c2.595 1.76 3.276 4.337 2.985 6.66-.608
 6.151-6.888 13.156-6.386 12.699 1.398-1.205 6.103-6.88
 6.987-12.2.888-5.316-3.586-7.159-3.586-7.159Zm-6.815 20.78L10.647
 24h2.599l.488-2.154h-3.566Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.coreldraw.com/en/learn/webinars/e'''

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
