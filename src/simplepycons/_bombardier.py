#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class BombardierIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bombardier"

    @property
    def original_file_name(self) -> "str":
        return "bombardier.svg"

    @property
    def title(self) -> "str":
        return "Bombardier"

    @property
    def primary_color(self) -> "str":
        return "#020203"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Bombardier</title>
     <path d="M0 10.422h1.232c.588 0 .859.308.859.785 0
 .336-.15.634-.495.7v.009c.411.047.588.392.588.71 0
 .54-.261.933-.942.933H0v-3.137zm.821 1.233h.197c.168 0
 .252-.15.252-.327 0-.177-.094-.327-.252-.327H.82v.654zm0
 1.325h.234c.15 0 .29-.14.29-.392
 0-.243-.14-.383-.29-.383H.82v.775zm2.708-2.614c.84 0 1.13.458 1.13
 1.634s-.29 1.634-1.13 1.634-1.12-.458-1.12-1.634.298-1.634
 1.12-1.634m0 2.717c.252 0
 .28-.234.28-1.083s-.019-1.083-.28-1.083-.28.234-.28 1.083.028
 1.083.28 1.083m1.437-2.66h1.176l.336
 1.866h.01l.336-1.867H8v3.137h-.756v-2.334h-.01l-.457
 2.334H6.19l-.439-2.334h-.009v2.334h-.756c-.019.01-.019-3.137-.019-3.137zm3.36
 0h1.242c.588 0 .85.307.85.784 0
 .336-.15.634-.495.7v.009c.41.047.588.392.588.71 0
 .54-.261.933-.943.933H8.327v-3.137zm.832 1.232h.196c.158 0
 .26-.15.26-.327 0-.177-.092-.327-.26-.327h-.196v.654zm0
 1.325h.233c.15 0 .29-.14.29-.392
 0-.243-.14-.383-.29-.383h-.233v.775zm2.175-2.558h1.026l.775
 3.137h-.877l-.084-.55h-.654l-.084.55h-.877l.775-3.137zm.513.645-.233
 1.334h.457l-.224-1.334zm1.503-.645h1.279c.625 0 .859.355.859.84 0
 .411-.16.691-.542.747v.01c.392.037.514.29.514.7v.261c0 .159 0
 .364.046.439a.18.18 0 0 0
 .094.093v.047h-.878c-.084-.159-.084-.457-.084-.598v-.205c0-.355-.065-.448-.261-.448h-.215v1.25h-.812v-3.136zm.812
 1.335h.159c.233 0 .345-.15.345-.382
 0-.252-.103-.364-.345-.364h-.159v.746zm1.68-1.335h1.186c.943 0
 .99.747.99 1.578s-.047 1.568-.99 1.568H15.84v-3.146zm.822
 2.558h.158c.327 0 .355-.14.355-.98
 0-.85-.037-.98-.355-.98h-.158v1.96zm1.69-2.558h.82v3.137h-.82v-3.137zm1.185
 0h1.867v.663H20.35v.542h.98v.644h-.98v.625h1.083v.663h-1.895v-3.137zm2.203
 0h1.279c.625 0 .859.355.859.84 0
 .411-.159.691-.532.747v.01c.392.037.513.29.513.7v.261c0 .159 0
 .364.047.439a.18.18 0 0 0
 .093.093v.047h-.877c-.084-.159-.084-.457-.084-.598v-.205c0-.355-.066-.448-.262-.448h-.215v1.25h-.812l-.009-3.136zm.821
 1.335h.16c.232 0 .345-.15.345-.382
 0-.252-.103-.364-.346-.364h-.159v.746z" />
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
