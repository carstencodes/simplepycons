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


class BitcometIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bitcomet"

    @property
    def original_file_name(self) -> "str":
        return "bitcomet.svg"

    @property
    def title(self) -> "str":
        return "BitComet"

    @property
    def primary_color(self) -> "str":
        return "#F49923"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>BitComet</title>
     <path d="M11.996 0C5.37.002.002 5.375.004 12v.009c.003 6.625
 5.375 11.993 12 11.991 6.625-.002 11.994-5.375 11.992-12v-.009C23.993
 5.366 18.62-.002 11.996 0zM3.008 14.396c.235-2.436.696-4.614
 1.422-6.467a15.261 15.261 0 0 1 2.238-2.406 16.578 16.578 0 0 0-1.68
 4.674c-.731 1.4-1.4 2.88-1.98 4.199zm6.06
 2.862c-.833-2.164-.764-4.942-.452-7.522a17.028 17.028 0 0 1
 1.661-2.777c.13.721.246 1.49.356 2.28-.841 2.033-1.457 4.722-1.564
 8.019zm6.64
 0c-.117-3.624-.853-6.498-1.824-8.587.087-.589.176-1.165.274-1.712.883
 1.19 1.561 2.484 2.114 3.82.204 2.268.159 4.604-.564
 6.479zm3.464-8.188a16.704 16.704 0 0 0-1.404-3.547c1.088.933 2.054
 2.054 2.928 3.383.527 1.629.878 3.47 1.073
 5.49-.739-1.68-1.621-3.623-2.597-5.326zm.83-1.945a16.735 16.735 0 0
 0-.84-.953l-.06-.057a15.323 15.323 0 0
 0-.87-.839c-.1-.087-.209-.167-.311-.253-.238-.2-.474-.4-.73-.587a14.579
 14.579 0 0
 0-1.176-.779c.218.307.423.612.616.917l.048.081c.175.279.342.556.497.834l.017.033c.333.598.621
 1.194.869 1.792 1.494 3.606 1.508 7.26.81
 11.522-.562-3.39-1.284-6.707-2.781-9.661a20.003 20.003 0 0
 0-1.028-1.783c-.088-.134-.184-.266-.277-.398a15.964 15.964 0 0
 0-.913-1.194c-.08.387-.154.8-.227 1.214-.05.288-.1.578-.146.875-.587
 3.696-.938 8.202-1.282
 12.078-.329-3.698-.664-7.967-1.203-11.562a65.458 65.458 0 0
 0-.205-1.283c-.079-.453-.16-.9-.247-1.322-.347.405-.66.825-.958
 1.252-.283.411-.546.832-.792 1.26-1.823 3.163-2.632 6.799-3.25
 10.524-.622-3.798-.672-7.112.38-10.34.256-.788.579-1.572.975-2.355l.091-.173c.162-.31.335-.622.52-.933l.16-.268c.228-.369.468-.738.731-1.11a14.497
 14.497 0 0
 0-1.433.982c-.21.16-.412.327-.61.496-.134.115-.272.229-.4.347-.253.232-.495.47-.728.715l-.007.007C3.63
 7.897 2.472 9.86 1.575 11.811 1.903 4.493 6.516.324 12.218.324c5.703
 0 10.315 4.169 10.643 11.488-.739-1.608-1.658-3.22-2.858-4.687z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://en.wikipedia.org/wiki/File:BitComet_l'''

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
