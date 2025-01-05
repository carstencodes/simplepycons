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


class EclipseVertdotxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "eclipsevertdotx"

    @property
    def original_file_name(self) -> "str":
        return "eclipsevertdotx.svg"

    @property
    def title(self) -> "str":
        return "Eclipse Vert.x"

    @property
    def primary_color(self) -> "str":
        return "#782A90"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Eclipse Vert.x</title>
     <path d="M3.356.01C1.566.01.027 1.269 0 2.938v1.436h2.515l3.861
 8.896 4.028-8.791h5.078l2.182 3.986 2.56-3.986H24V2.946C24 1.281
 22.44.011 20.645.011zM24 5.668l-8.874
 13.56H12.44c-.02-.629-.188-1.237-.503-1.74l3.609-5.708-2.744-4.36-3.829
 8.42-.036-.002a3.443 3.443 0 0 0-3.434 3.433c0
 .021.003.042.004.063h-.263L0 7.5v13.553c0 1.665 1.56 2.935 3.356
 2.935h17.289c1.812 0 3.355-1.276
 3.355-2.935v-1.826h-3.587l-1.594-2.874 2.224-3.378L24 17.638zm-15.066
 11.5a2.102 2.102 0 0 1 2.109 2.103 2.106 2.106 0 1 1-4.212
 0c0-1.16.937-2.1 2.103-2.103Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/vert-x3/.github/blob/1ad66
12d87f35665e50a00fc32eb9c542556385d/workflow-templates/vertx-favicon.s'''

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
