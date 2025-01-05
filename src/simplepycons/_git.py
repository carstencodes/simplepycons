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


class GitIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "git"

    @property
    def original_file_name(self) -> "str":
        return "git.svg"

    @property
    def title(self) -> "str":
        return "Git"

    @property
    def primary_color(self) -> "str":
        return "#F05032"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Git</title>
     <path d="M23.546 10.93L13.067.452c-.604-.603-1.582-.603-2.188
 0L8.708 2.627l2.76 2.76c.645-.215 1.379-.07 1.889.441.516.515.658
 1.258.438 1.9l2.658 2.66c.645-.223 1.387-.078 1.9.435.721.72.721
 1.884 0 2.604-.719.719-1.881.719-2.6
 0-.539-.541-.674-1.337-.404-1.996L12.86
 8.955v6.525c.176.086.342.203.488.348.713.721.713 1.883 0
 2.6-.719.721-1.889.721-2.609 0-.719-.719-.719-1.879
 0-2.598.182-.18.387-.316.605-.406V8.835c-.217-.091-.424-.222-.6-.401-.545-.545-.676-1.342-.396-2.009L7.636
 3.7.45 10.881c-.6.605-.6 1.584 0 2.189l10.48 10.477c.604.604
 1.582.604 2.186 0l10.43-10.43c.605-.603.605-1.582 0-2.187" />
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
